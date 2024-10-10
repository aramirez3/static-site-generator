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

def block_to_block_types(md_block):
    lines = md_block.split("\n")
    if md_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockTypes.HEADING.value

    if md_block.startswith("```"):
        if len(lines) > 1 and lines[0].startswith("```") and lines[-1]:
            return BlockTypes.CODE.value

    if md_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockTypes.PARAGRAPH.value
        return BlockTypes.QUOTE.value

    if md_block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockTypes.PARAGRAPH.value
        return BlockTypes.UNORDERED_LIST.value
    
    if md_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockTypes.PARAGRAPH.value
        return BlockTypes.UNORDERED_LIST.value

    if md_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockTypes.PARAGRAPH.value
            i += 1
        return BlockTypes.ORDERED_LIST.value

    return BlockTypes.PARAGRAPH.value
