#!/bin/bash

tmux kill-server 2>/dev/null || true

cd /root/MLH-portfolio
git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s flask -c /root/MLH-portfolio \
  'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
