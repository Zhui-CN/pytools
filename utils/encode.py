def encode(text):
    if not isinstance(text, bytes):
        text = bytes(text, "utf-8")
    return text
