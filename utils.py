def clean_output(text):
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if any(p in line for p in ["New llama.cpp version", "To update, run", "In order to exit"]):
            continue
        if line in ("exit()", ""):
            continue
        if line.startswith(">"):
            line = line[1:].lstrip()
        cleaned.append(line)
    return "\n".join(cleaned).strip()