#!/bin/bash

echo "starting paperbenni's meme discord bot"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
echo "$DIR"
cd "$DIR"

git pull

if ! [ -e .discord ]; then
    echo "discord token not found"
    sleep 1m
    exit 1
fi

while :; do
    python3 mainbot.py
    echo "crashed"
    sleep 1
done
