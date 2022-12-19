#!/bin/bash

if [ -d ".venv" ]
then
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 freeze.py
else
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python3  freeze.py
fi
