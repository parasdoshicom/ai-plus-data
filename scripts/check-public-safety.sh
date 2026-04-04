#!/usr/bin/env bash

set -euo pipefail

if ! command -v rg >/dev/null 2>&1; then
  echo "ripgrep (rg) is required for public-safety checks." >&2
  exit 1
fi

declare -a files=()
while IFS= read -r -d '' file; do
  files+=("$file")
done < <(git ls-files -z)

if [ ${#files[@]} -eq 0 ]; then
  echo "No tracked files to scan."
  exit 0
fi

checks=(
  "GitHub PAT|ghp_[A-Za-z0-9]{36}"
  "GitHub fine-grained PAT|github_pat_[A-Za-z0-9_]{20,}"
  "OpenAI key|sk-[A-Za-z0-9]{20,}"
  "Slack token|xox[baprs]-[A-Za-z0-9-]{10,}"
  "AWS access key|AKIA[0-9A-Z]{16}"
  "Private key block|-----BEGIN (OPENSSH|RSA|DSA|EC|PGP) PRIVATE KEY-----"
  "Credential assignment|(?i)(api[_-]?key|secret|token|password)\\s*[:=]\\s*[\"'][^\"'\\n]{8,}[\"']"
  "Telegram bot token|[0-9]{8,10}:[A-Za-z0-9_-]{35}"
  "Operational ID wiring|(?i)(chat[_ -]?id|thread[_ -]?id|sender[_ -]?id)\\s*[:=]\\s*[\"']?-?[0-9]{6,}[\"']?"
  "Slack workspace link|https://[^ )]*slack\\.com/"
  "Private dashboard link|https://[^ )]*(looker|mode\\.com|metabase|superset)[^ )]*"
)

failures=0

for rule in "${checks[@]}"; do
  label=${rule%%|*}
  regex=${rule#*|}

  if rg --pcre2 -n -I --color=never "$regex" "${files[@]}" >/tmp/ai_plus_data_public_safety_match.txt 2>/dev/null; then
    failures=1
    echo
    echo "[FAIL] ${label}"
    cat /tmp/ai_plus_data_public_safety_match.txt
  fi
done

rm -f /tmp/ai_plus_data_public_safety_match.txt

if [ "$failures" -ne 0 ]; then
  echo
  echo "Public-safety checks failed. Remove private runtime details, credentials, or operational identifiers before publishing."
  exit 1
fi

echo "Public-safety checks passed."
