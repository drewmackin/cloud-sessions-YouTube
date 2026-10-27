# shellcheck shell=bash
# Shared Docker helpers, sourced by the tool wrappers.
# Cloud sessions start with Docker installed but its daemon stopped, so start it on demand.

ensure_docker() {
  if ! command -v docker >/dev/null 2>&1; then
    echo "Docker is not installed. On your own computer install Docker Desktop; cloud sessions already have it." >&2
    return 1
  fi
  docker info >/dev/null 2>&1 && return 0
  if [[ $(id -u) -eq 0 ]] && command -v dockerd >/dev/null 2>&1; then
    (nohup dockerd >"${TMPDIR:-/tmp}/dockerd.log" 2>&1 &)
    for _ in $(seq 1 30); do
      docker info >/dev/null 2>&1 && return 0
      sleep 1
    done
  fi
  echo "The Docker daemon is not running. Start Docker, then retry." >&2
  return 1
}

# Containers don't inherit the session's egress proxy. When one is configured (cloud sessions), share the
# host network so 127.0.0.1:<proxy> is reachable, forward the proxy variables and trust the proxy's CA.
# Sets the PROXY_ARGS array for `docker run`.
proxy_args() {
  PROXY_ARGS=()
  [[ -n "${HTTPS_PROXY:-${https_proxy:-}}" ]] || return 0
  PROXY_ARGS+=(--network host)
  local var
  for var in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy JAVA_TOOL_OPTIONS; do
    [[ -n "${!var:-}" ]] && PROXY_ARGS+=(-e "$var")
  done
  local ca="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}"
  if [[ -f "$ca" ]]; then
    PROXY_ARGS+=(-v "$ca:/etc/ssl/proxy-ca.crt:ro" -e SSL_CERT_FILE=/etc/ssl/proxy-ca.crt)
  fi
  if [[ -f /etc/ssl/certs/java/cacerts ]]; then
    PROXY_ARGS+=(-v /etc/ssl/certs/java/cacerts:/etc/ssl/certs/java/cacerts:ro)
  fi
}

ensure_image() {
  local image="$1"
  docker image inspect "$image" >/dev/null 2>&1 && return 0
  echo "Pulling $image (first use in this session)…" >&2
  docker pull --quiet "$image" >&2
}
