from utilities import *

def markdown_to_blocks(text):
    lines = text.split("\n\n")
    blocks = []
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks