from utilities import *

from parentnode import ParentNode
from md_inlines import text_to_textnodes, text_node_to_html_node

def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
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
        if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        node = block_to_html_node(block)
        child_nodes.append(node)
        print(f"child node in {block}::\n:::::{node}")
    return ParentNode("div", child_nodes)

def block_to_html_node(block):
    block_type = block_to_block_types(block)
    if block_type == BlockTypes.PARAGRAPH.value:
        return paragraph_to_html_node(block)
    if block_type == BlockTypes.HEADING.value:
        return heading_to_html_node(block)
    if block_type == BlockTypes.QUOTE.value:
        return quote_to_html_node(block)
    if block_type == BlockTypes.CODE.value:
        return code_to_html_node(block)
    if block_type == BlockTypes.UNORDERED_LIST.value:
        return unordered_list_to_html_node(block)
    if block_type == BlockTypes.ORDERED_LIST.value:
        return ordered_list_to_html_node(block)
    pass

def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    h_level = 0
    for ch in block:
        if ch == "#":
            h_level += 1
    if h_level + 1 > len(block):
        raise ValueError(f"Invalid heading level {h_level}")
    text = block[h_level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{h_level}", children)

def quote_to_html_node(block):
    text = block.split("> ")
    children = text_to_children(text[1])
    return ParentNode("blockquote", children)

def code_to_html_node(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Invalid code block")
    children = text_to_children(block[4:-4])
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    print(lines)

def unordered_list_to_html_node(block):
    return block