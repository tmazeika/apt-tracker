#!/usr/bin/env bash

set -e

mkdir -p out
FILENAME="out/`date '+%Y-%m-%d %H:%M:%S'`.json"

set -o pipefail
python3 -u main.py | tee "$FILENAME"
set +o pipefail

curl -X POST 'https://prqtulnbkrgpznjvscje.supabase.co/rest/v1/apartments' \
    -H "apikey: $SUPABASE_KEY" \
    -H "Authorization: Bearer $SUPABASE_KEY" \
    -H "Content-Type: application/json" \
    -d "`cat "$FILENAME" | jq -s`"
