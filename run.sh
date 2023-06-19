#!/usr/bin/env bash

python3 -u main.py | tee "`date '+%Y-%m-%d %H:%M:%S'`.csv"