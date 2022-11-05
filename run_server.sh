#!/bin/zsh

python3 -m uvicorn server:app --host="0.0.0.0" --port="5003"
