def extract_title(markdown):
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise ValueError("Title (h1) is required")
    else:
        return lines[0].split('# ')[1]