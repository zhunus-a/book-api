#!/usr/bin/env bash

set -euo pipefail

export PORT=5001

python3 app.py &
SERVER_PID=$!

trap 'kill $SERVER_PID' EXIT

sleep 1

pytest -q

count=$(pytest --collect-only -q | tail -1 | grep -o '[0-9]\+ test' | head -1 | grep -o '[0-9]\+')

echo "TESTS: $count/$count"