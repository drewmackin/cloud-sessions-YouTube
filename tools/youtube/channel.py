#!/usr/bin/env python3
"""Inventory a YouTube channel with the YouTube Data API v3: stats plus every upload.

  python3 tools/youtube/channel.py @handle --out research/<person>/youtube
  python3 tools/youtube/channel.py https://www.youtube.com/@handle --out ...
  python3 tools/youtube/channel.py UCxxxxxxxxxxxxxxxxxxxxxx --out ...
  python3 tools/youtube/channel.py "Person Name" --search --out ...   # costs 100 quota units

Writes channel.md (stats, most-viewed, most-recent, full list), videos.json and videos.csv.
Needs YOUTUBE_API_KEY (free; 10,000 quota units a day). A full inventory costs about
1 unit per 25 videos. www.googleapis.com is reachable from cloud sessions on the default
network setting. Standard library only; the key travels in a header and is never printed.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

API = "https://www.googleapis.com/youtube/v3"
DURATION_RE = re.compile(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


class ApiError(RuntimeError):
    pass


def api_get(endpoint: str, params: dict, key: str) -> dict:
    request = Request(f"{API}/{endpoint}?{urlencode(params)}", headers={"X-Goog-Api-Key": key})
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        try:
            message = json.load(exc)["error"]["message"]
        except (ValueError, KeyError, TypeError):
            message = exc.reason
        raise ApiError(f"YouTube API {endpoint}: HTTP {exc.code}: {message}".replace(key, "[key]")) from None
    except URLError as exc:
        raise ApiError(f"Can't reach {API}: {exc.reason}") from None


def parse_target(target: str) -> tuple[str, str]:
    """Return (lookup_field, value) for channels.list."""
    target = target.strip()
    if re.fullmatch(r"UC[\w-]{22}", target):
        return "id", target
    if target.startswith("@"):
        return "forHandle", target
    if "youtube.com" in target or "youtu.be" in target:
        path = urlsplit(target if "://" in target else "https://" + target).path.strip("/").split("/")
        if path and path[0].startswith("@"):
            return "forHandle", path[0]
        if len(path) >= 2 and path[0] == "channel":
            return "id", path[1]
        if len(path) >= 2 and path[0] == "user":
            return "forUsername", path[1]
        if len(path) >= 2 and path[0] == "c":
            return "search", path[1]
    return "search", target


def resolve_channel(target: str, key: str, allow_search: bool) -> dict:
    field, value = parse_target(target)
    if field == "search":
        if not allow_search:
            sys.exit(f"'{target}' is not a handle, channel id or channel URL. Pass --search to look it up "
                     "(costs 100 of the 10,000 daily quota units).")
        found = api_get("search", {"part": "snippet", "type": "channel", "q": value, "maxResults": 5}, key)
        items = found.get("items") or []
        if not items:
            sys.exit(f"No channel found for '{value}'.")
        print("Search matches (using the first):", file=sys.stderr)
        for item in items:
            print(f"  {item['snippet']['channelId']}  {item['snippet']['title']}", file=sys.stderr)
        field, value = "id", items[0]["snippet"]["channelId"]
    data = api_get("channels", {"part": "snippet,statistics,contentDetails,brandingSettings", field: value}, key)
    items = data.get("items") or []
    if not items:
        sys.exit(f"No channel found for {field}={value}.")
    return items[0]


def seconds(iso: str) -> int:
    match = DURATION_RE.fullmatch(iso or "")
    if not match:
        return 0
    days, hours, minutes, secs = (int(g or 0) for g in match.groups())
    return ((days * 24 + hours) * 60 + minutes) * 60 + secs


def clock(total: int) -> str:
    hours, rest = divmod(total, 3600)
    return f"{hours}:{rest // 60:02d}:{rest % 60:02d}" if hours else f"{rest // 60}:{rest % 60:02d}"


def list_uploads(channel: dict, key: str, limit: int) -> list[dict]:
    playlist = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    ids: list[str] = []
    page = None
    while len(ids) < limit:
        params = {"part": "contentDetails", "playlistId": playlist, "maxResults": 50}
        if page:
            params["pageToken"] = page
        data = api_get("playlistItems", params, key)
        ids += [item["contentDetails"]["videoId"] for item in data.get("items", [])]
        page = data.get("nextPageToken")
        if not page:
            break
    ids = ids[:limit]
    videos = []
    for start in range(0, len(ids), 50):
        data = api_get("videos", {"part": "snippet,statistics,contentDetails", "id": ",".join(ids[start:start + 50])}, key)
        for item in data.get("items", []):
            snippet, stats = item["snippet"], item.get("statistics", {})
            videos.append({
                "id": item["id"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "title": snippet.get("title", ""),
                "published": snippet.get("publishedAt", ""),
                "duration_s": seconds(item.get("contentDetails", {}).get("duration", "")),
                "views": int(stats.get("viewCount", 0) or 0),
                "likes": int(stats.get("likeCount", 0) or 0),
                "comments": int(stats.get("commentCount", 0) or 0),
                "live": snippet.get("liveBroadcastContent", "none"),
                "description": " ".join((snippet.get("description") or "").split())[:400],
            })
    return videos


def write_outputs(out: Path, channel: dict, videos: list[dict]) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "videos.json").write_text(json.dumps({"channel": channel, "videos": videos}, indent=2), encoding="utf-8")
    with (out / "videos.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(videos[0].keys()) if videos else ["id"])
        writer.writeheader()
        writer.writerows(videos)

    snippet, stats = channel["snippet"], channel.get("statistics", {})
    handle = snippet.get("customUrl", "")
    total_s = sum(v["duration_s"] for v in videos)
    shorts = sum(1 for v in videos if 0 < v["duration_s"] <= 60)

    def rows(items: list[dict]) -> list[str]:
        return [f"| {v['published'][:10]} | [{v['title'].replace('|', '/')}]({v['url']}) | {clock(v['duration_s'])} "
                f"| {v['views']:,} | {v['likes']:,} | {v['comments']:,} |" for v in items]

    header = ["| published | title | length | views | likes | comments |", "|---|---|---|---|---|---|"]
    by_views = sorted(videos, key=lambda v: -v["views"])
    by_date = sorted(videos, key=lambda v: v["published"], reverse=True)
    doc = [
        f"# YouTube channel: {snippet.get('title', '')} {handle}",
        "",
        f"https://www.youtube.com/channel/{channel['id']} · created {snippet.get('publishedAt', '')[:10]} "
        f"· country {snippet.get('country', 'n/a')}",
        "",
        f"- Subscribers: {int(stats.get('subscriberCount', 0) or 0):,}"
        + (" (hidden by the channel)" if stats.get("hiddenSubscriberCount") else ""),
        f"- Lifetime views: {int(stats.get('viewCount', 0) or 0):,} · public videos: {int(stats.get('videoCount', 0) or 0):,}",
        f"- Inventoried here: {len(videos):,} uploads, {total_s / 3600:,.1f} hours, {shorts} Shorts-length (≤60 s)",
        f"- Retrieved {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC via YouTube Data API v3",
        "",
        "## Channel description",
        "",
        "> " + " ".join((snippet.get("description") or "_none_").split()),
        "",
        "## Most viewed (top 25)",
        "",
        *header, *rows(by_views[:25]),
        "",
        "## Most recent (25)",
        "",
        *header, *rows(by_date[:25]),
        "",
        f"## All uploads ({len(videos)}, newest first)",
        "",
        *header, *rows(by_date),
    ]
    (out / "channel.md").write_text("\n".join(doc) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("channel", help="@handle, channel URL, channel id (UC…), or a name with --search")
    parser.add_argument("--out", required=True, help="output folder, e.g. research/<person>/youtube")
    parser.add_argument("--search", action="store_true", help="allow a name search (100 quota units)")
    parser.add_argument("--max-videos", type=int, default=2000)
    args = parser.parse_args(argv)
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if not key:
        sys.exit("YOUTUBE_API_KEY is not set. See README.md, 'Keys and settings'.")
    try:
        channel = resolve_channel(args.channel, key, args.search)
        videos = list_uploads(channel, key, args.max_videos)
    except ApiError as exc:
        sys.exit(str(exc))
    write_outputs(Path(args.out), channel, videos)
    print(f"{channel['snippet']['title']}: {len(videos)} videos → {args.out}/channel.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
