#!/bin/bash
set -e

if [ ! -f .env ]; then
    touch .env
fi

pip install --upgrade pip
pip install -r requirements.txt

echo "[install.sh] Dependencies installed."
