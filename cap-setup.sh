#!/usr/bin/env bash
# First-time Capacitor setup script.
# Run once after cloning: bash cap-setup.sh
set -e

echo "→ Installing npm dependencies..."
npm install

echo "→ Setting up Python virtualenv..."
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt -q

echo "→ Building the site..."
.venv/bin/python3 scripts/build.py

echo "→ Adding iOS platform..."
npx cap add ios

echo "→ Adding Android platform..."
npx cap add android

echo "→ Syncing web assets into native projects..."
npx cap sync

echo ""
echo "Done. Next steps:"
echo "  iOS:     npm run open:ios     (requires Xcode)"
echo "  Android: npm run open:android (requires Android Studio)"
