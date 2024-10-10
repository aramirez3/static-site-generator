from utilities import *
import re

regex_values = {
    "headings": r"^(#{1,6})\s",
    "code": r"^(\`{3}).*\`{3}",
    "quote": r"^(\>{1}.*)",
    "unordered_list": r"^(\-|\*)\s",
    "ordered_list": "working on this piece"
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
    if re.match(regex_values["headings"], md_line):
        return BlockTypes.HEADING.value
    if re.match(regex_values["code"], md_line):
        return BlockTypes.CODE.value
    if re.match(regex_values["quote"], md_line):
        return BlockTypes.QUOTE.value
    if re.search(regex_values["unordered_list"], md_line):
        return BlockTypes.UNORDERED_LIST.value
    if re.search(regex_values["ordered_list"], md_line):
        return BlockTypes.ORDERED_LIST.value
    return BlockTypes.PARAGRAPH.value
