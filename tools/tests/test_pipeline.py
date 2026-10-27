"""Offline self-tests for the research toolkit: python3 -m unittest discover tools/tests"""
from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools" / "discord"), str(ROOT / "tools" / "youtube")]

import channel  # noqa: E402
import intel  # noqa: E402

TARGET_ID = "500000000000000001"


def run(fn, argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = fn(argv)
    return code, out.getvalue()


class DiscordIntelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.export = Path(cls.tmp.name) / "export"
        subprocess.run([sys.executable, str(ROOT / "tools/discord/testdata/make_sample_export.py"), str(cls.export)],
                       check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_profile_builds_full_evidence_pack(self):
        out = Path(self.tmp.name) / "pack"
        code, _ = run(intel.main, ["profile", str(self.export), "--target", "marcus.hale", "--out", str(out)])
        self.assertEqual(code, 0)
        for name in ["overview.md", "messages-001.md", "qa.md", "links.md", "people.md", "pinned.md",
                     "announcements-001.md", "youtube_links.txt", "target_messages.jsonl", "index.json"]:
            self.assertTrue((out / name).is_file(), name)
        summary = json.loads((out / "index.json").read_text())
        self.assertEqual(summary["targets"], [TARGET_ID])
        self.assertEqual(summary["target_messages"], 149)
        self.assertEqual(summary["replies_made"], 101)
        self.assertGreater(summary["replies_received"], 0)
        youtube = (out / "youtube_links.txt").read_text().split()
        self.assertIn("https://www.youtube.com/watch?v=BBBBBBBBBBB", youtube)  # from a youtu.be link
        self.assertIn("https://www.youtube.com/watch?v=CCCCCCCCCCC", youtube)  # from a /live/ link
        self.assertEqual(len(youtube), len(set(youtube)))
        links = (out / "links.md").read_text()
        listed = [line.split(" — ")[0] for line in links.splitlines() if line.startswith("- http")]
        self.assertIn("- https://docs.google.com/spreadsheets/d/sample-sheet-id/edit", listed)  # utm_ stripped
        self.assertIn("- https://youtu.be/BBBBBBBBBBB", listed)  # si= stripped; quotes stay verbatim
        jsonl = (out / "target_messages.jsonl").read_text().splitlines()
        self.assertEqual(len(jsonl), 149)
        self.assertIn("q3-chart.png", (out / "messages-001.md").read_text())  # attachment-only message kept

    def test_profile_chunks_long_histories(self):
        out = Path(self.tmp.name) / "chunked"
        run(intel.main, ["profile", str(self.export), "--target", TARGET_ID, "--out", str(out), "--chunk-chars", "5000"])
        parts = sorted(out.glob("messages-*.md"))
        self.assertGreater(len(parts), 3)
        self.assertTrue(all(len(p.read_text()) < 9000 for p in parts))

    def test_ambiguous_target_lists_candidates(self):
        with self.assertRaises(SystemExit) as ctx:
            run(intel.main, ["profile", str(self.export), "--target", "a", "--out", self.tmp.name + "/x"])
        self.assertIn("matches", str(ctx.exception))
        self.assertIn(TARGET_ID, str(ctx.exception))

    def test_bots_and_system_messages_are_not_target_content(self):
        corpus = intel.load([str(self.export)])
        joins = [m for m in corpus.messages.values() if m.kind == "GuildMemberJoin"]
        self.assertEqual(len(joins), 1)
        self.assertTrue(joins[0].author_is_bot)

    def test_search_returns_context_and_respects_limit(self):
        code, text = run(intel.main, ["search", str(self.export), "-q", "65%", "--author", TARGET_ID, "--limit", "3"])
        self.assertEqual(code, 0)
        self.assertEqual(text.count("## Match"), 3)
        self.assertIn("showing the first 3 of", text)
        self.assertIn("▶", text)

    def test_rejects_non_dce_json(self):
        bad = Path(self.tmp.name) / "bad.json"
        bad.write_text('{"hello": 1}')
        with self.assertRaises(SystemExit):
            intel.load([str(bad)])

    def test_clean_url(self):
        self.assertEqual(intel.clean_url("https://YouTu.be/abc?si=xyz&t=30)."), "https://youtu.be/abc?t=30")
        self.assertEqual(intel.clean_url("https://x.com/a?utm_source=d&id=2"), "https://x.com/a?id=2")


class YouTubeChannelTest(unittest.TestCase):
    CHANNEL = {"id": "UC1234567890123456789012",
               "snippet": {"title": "Sample Channel", "customUrl": "@sample", "publishedAt": "2019-05-01T00:00:00Z",
                           "description": "Real estate investing."},
               "statistics": {"subscriberCount": "12345", "viewCount": "999999", "videoCount": "3"},
               "contentDetails": {"relatedPlaylists": {"uploads": "UU1234567890123456789012"}}}

    def fake_api(self, endpoint, params, key):
        self.assertEqual(key, "test-key")
        if endpoint == "channels":
            self.assertEqual(params.get("forHandle"), "@sample")
            return {"items": [self.CHANNEL]}
        if endpoint == "playlistItems":
            return {"items": [{"contentDetails": {"videoId": v}} for v in ["vid00000001", "vid00000002", "vid00000003"]]}
        if endpoint == "videos":
            return {"items": [
                {"id": "vid00000001", "snippet": {"title": "Deal breakdown | duplex", "publishedAt": "2026-01-02T00:00:00Z"},
                 "statistics": {"viewCount": "5000", "likeCount": "200", "commentCount": "30"},
                 "contentDetails": {"duration": "PT14M5S"}},
                {"id": "vid00000002", "snippet": {"title": "Short tip", "publishedAt": "2026-03-01T00:00:00Z"},
                 "statistics": {"viewCount": "90000"}, "contentDetails": {"duration": "PT45S"}},
                {"id": "vid00000003", "snippet": {"title": "Live Q&A", "publishedAt": "2025-11-11T00:00:00Z"},
                 "statistics": {"viewCount": "700"}, "contentDetails": {"duration": "PT1H30M"}},
            ]}
        raise AssertionError(endpoint)

    def test_inventory_from_handle(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(channel, "api_get", self.fake_api), \
                mock.patch.dict("os.environ", {"YOUTUBE_API_KEY": "test-key"}):
            code, _ = run(channel.main, ["@sample", "--out", tmp])
            self.assertEqual(code, 0)
            doc = (Path(tmp) / "channel.md").read_text()
            self.assertIn("Subscribers: 12,345", doc)
            self.assertIn("1 Shorts-length", doc)
            self.assertIn("Deal breakdown / duplex", doc)  # pipe escaped for the table
            most_viewed = doc.split("## Most viewed")[1].split("## Most recent")[0]
            self.assertLess(most_viewed.index("Short tip"), most_viewed.index("Deal breakdown"))
            rows = (Path(tmp) / "videos.csv").read_text().splitlines()
            self.assertEqual(len(rows), 4)


if __name__ == "__main__":
    unittest.main()
