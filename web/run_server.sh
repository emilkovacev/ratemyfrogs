#!/bin/bash

python3 -m uvicorn server:app --host="0.0.0.0" --port="5000"
