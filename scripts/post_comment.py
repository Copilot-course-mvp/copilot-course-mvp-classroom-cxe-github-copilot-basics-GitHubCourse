#!/usr/bin/env python3
"""Post or update a single bot comment on a GitHub PR.

Uses a hidden HTML marker to find and update an existing comment
instead of creating duplicates on each push.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error


MARKER_TEMPLATE = "<!-- {marker} -->"


def _github_api(method: str, url: str, body: dict | None = None) -> dict | list:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def _find_existing_comment(repo: str, pr: int, marker: str) -> int | None:
    """Return the comment id that contains the marker, or None."""
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/issues/{pr}/comments?per_page=100&page={page}"
        comments = _github_api("GET", url)
        if not comments:
            break
        for comment in comments:
            if marker in comment.get("body", ""):
                return comment["id"]
        page += 1
    return None


def post_or_update(repo: str, pr: int, marker_name: str, body: str) -> None:
    marker = MARKER_TEMPLATE.format(marker=marker_name)
    full_body = f"{marker}\n{body}"

    existing_id = _find_existing_comment(repo, pr, marker)
    if existing_id:
        url = f"https://api.github.com/repos/{repo}/issues/comments/{existing_id}"
        _github_api("PATCH", url, {"body": full_body})
        print(f"Updated comment {existing_id}")
    else:
        url = f"https://api.github.com/repos/{repo}/issues/{pr}/comments"
        result = _github_api("POST", url, {"body": full_body})
        print(f"Created comment {result['id']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Post/update a PR comment")
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--pr", required=True, type=int, help="PR number")
    parser.add_argument("--marker", required=True, help="Unique marker name for this comment")
    parser.add_argument("--body", required=True, help="Comment body (Markdown)")
    args = parser.parse_args()

    try:
        post_or_update(args.repo, args.pr, args.marker, args.body)
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error: {exc.code} {exc.reason}", file=sys.stderr)
        body = exc.read().decode()
        print(body, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
