import re, json

def extract_first_json(text):
    match = re.search(r"\{[\s\S]*?\}", text)
    if not match:
        raise ValueError("No JSON found")
    return json.loads(match.group())