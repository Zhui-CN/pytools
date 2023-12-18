import json


def parse_headers(text):
    headers = {}
    for header in text.strip().split("\n"):
        if not header:
            continue
        key, value = header.split(':', 1)
        # new_key = "-".join([k.capitalize().strip() for k in key.split("-")])
        new_key = key
        headers[new_key] = value.strip()
    return json.dumps(headers, ensure_ascii=False, indent=4)
