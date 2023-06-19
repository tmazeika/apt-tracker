# apt-tracker

### Running
To run without uploading results:

```bash
python3 main.py
```

To run and upload results to Supabase:

```bash
echo "export SUPABASE_KEY=<key>" > .env
source .env
./run.sh
```