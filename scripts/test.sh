#!/usr/bin/env bash

set -euo pipefail

export PORT=5001

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

venv/bin/python -m pip install -q -r requirements.txt

venv/bin/python app.py &
SERVER_PID=$!

trap 'kill $SERVER_PID' EXIT

sleep 1

venv/bin/python -m pytest -q

count=$(venv/bin/python -m pytest --collect-only -q | tail -1 | grep -o '[0-9]\+ test' | head -1 | grep -o '[0-9]\+')

echo "TESTS: $count/$count"
