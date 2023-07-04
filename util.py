import re


def extract_int(text: str) -> int:
    return int(re.search(r'(\d+)', text.replace(',', '')).group(1))
