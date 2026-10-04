#!/usr/bin/env bash

set -euo pipefail

PORT="${PORT:-8080}"

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

venv/bin/python -m pip install -q -r requirements.txt

venv/bin/python app.py
