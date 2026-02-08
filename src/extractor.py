def extract_fields(text):
    extracted = {}

    for line in text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            extracted[key.strip()] = value.strip()

    return extracted
