#!/usr/bin/env python3
"""
Send a weekly push notification to all subscribed devices via FCM.
Run every Friday by .github/workflows/parasha-push.yml.

Requires:
  FIREBASE_SERVER_KEY env var — Legacy FCM server key from Firebase Console
  FCM_TOPIC env var         — Topic name (default: parasha_weekly)
"""
import json
import os
import datetime
import requests
import frontmatter
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
ARTICLES_JSON = Path(__file__).parent.parent / "docs" / "articles.json"


def find_current_parasha():
    """Return the most recent article whose date is on or before today."""
    today = datetime.date.today()
    candidates = []

    for md_file in CONTENT_DIR.glob("*.md"):
        try:
            post = frontmatter.load(md_file)
            date_val = post.get("date")
            if not date_val:
                continue
            if isinstance(date_val, str):
                date_val = datetime.date.fromisoformat(date_val)
            if isinstance(date_val, datetime.datetime):
                date_val = date_val.date()
            if date_val <= today:
                candidates.append({
                    "date": date_val,
                    "slug": md_file.stem,
                    "title": post.get("title", ""),
                    "parasha": post.get("parasha", ""),
                    "excerpt": post.get("excerpt", "")[:100],
                })
        except Exception as e:
            print(f"[warn] Skipping {md_file.name}: {e}")

    if not candidates:
        raise RuntimeError("No articles found for today")

    candidates.sort(key=lambda a: a["date"], reverse=True)
    return candidates[0]


def send_fcm(article):
    server_key = os.environ["FIREBASE_SERVER_KEY"]
    topic = os.environ.get("FCM_TOPIC", "parasha_weekly")

    payload = {
        "to": f"/topics/{topic}",
        "notification": {
            "title": article["parasha"] or article["title"],
            "body": article["excerpt"],
        },
        "data": {
            "slug": article["slug"],
            "url": f"/parasha/{article['slug']}.html",
        },
        "android": {
            "priority": "high",
            "notification": {"channel_id": "parasha_weekly"},
        },
        "apns": {
            "payload": {"aps": {"sound": "default", "badge": 1}},
        },
    }

    resp = requests.post(
        "https://fcm.googleapis.com/fcm/send",
        headers={
            "Authorization": f"key={server_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
        timeout=15,
    )
    resp.raise_for_status()
    result = resp.json()
    if result.get("failure"):
        raise RuntimeError(f"FCM error: {result}")
    print(f"[push] Sent: {article['title']} → topic/{topic} | FCM: {result}")


if __name__ == "__main__":
    article = find_current_parasha()
    print(f"[push] Current parasha: {article['parasha']} ({article['date']})")
    send_fcm(article)
