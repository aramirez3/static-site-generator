from utilities import *

from md_blocks import *
from htmlnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    
    for block in blocks:
        block_type = block_to_block_types(block)
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
            block_text = remove_leading_chars_single_line(block, regex_values[block_type])
            return block_text
        case BlockTypes.CODE.value:
            block_text = ""
            return block_text
        case BlockTypes.QUOTE.value:
            block_text = remove_leading_chars_single_line(block, "> ")
            return block_text
        case BlockTypes.UNORDERED_LIST.value:
            block_text = remove_leading_chars_list(block, block_type)
            return block_text
        case BlockTypes.ORDERED_LIST.value:
            block_text = remove_leading_chars_list(block, block_type)
            return block_text

def remove_leading_chars_single_line(block, regex):
    loc = regex_match(regex, block).span()
    return block[loc[1]+1:]

def remove_leading_chars_list(block, block_type):
    text = ""
    return text

def remove_leading_chars_code(block):
    text = ""
    return text