from utilities import *

from md_blocks import *
from htmlnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    
    for block in blocks:
        block_type = block_to_block_types(block)
        print(f"block::{block_type}:: {block} ")
        node = block_to_html(block, block_type)
        ## get children from block text
        html_nodes.append(node)
    return html_nodes

def block_to_html(block, block_type):
    tag = None
    block_tags = get_block_tags()
    value = get_block_text(block, block_type)
    
    if block_type == BlockTypes.HEADING.value:
        h_type = get_heading_type(block)
        tag = block_tags[block_type][h_type]
    ## need to add case for ordered & unordered lists
    else:
        tag = block_tags[block_type]
    
    node = HTMLNode(tag, value)
    return node

def get_heading_type(text):
    h_span = re.match("#", text).span()
    len = h_span[1] - h_span[0]
    return f"h{len}"

def text_to_children(text):
    pass

def get_block_text(block, block_type):
    match block_type:
        case BlockTypes.PARAGRAPH.value:
            return block
        case BlockTypes.HEADING.value:
            prefix = re.match(r"(\#{1,6}\s)", block).group(1)
            return block.removeprefix(prefix)
        case BlockTypes.CODE.value:
            block = block.removeprefix("```")
            block = block.removesuffix("```")
            return block
        case BlockTypes.QUOTE.value:
            return block.removeprefix("> ")
        case BlockTypes.UNORDERED_LIST.value:
            return block
        case BlockTypes.ORDERED_LIST.value:
            return block