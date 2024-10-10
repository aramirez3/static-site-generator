from utilities import *
import re

regex_values = {
    "headings": r"^(#{1,6})\s",
    "code": r"^(\`{3}).*\`{3}",
}

def markdown_to_blocks(md):
    lines = md.split("\n\n")
    blocks = []
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks

def block_to_block_types(md_line):
    match md_line:
        case s if re.match(regex_values["headings"], s):
            return BlockTypes.HEADING.value
        case s if re.match(regex_values["code"], s):
            return BlockTypes.CODE.value
        case _:
            return BlockTypes.PARAGRAPH.value
