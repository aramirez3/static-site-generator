from utilities import *

from md_blocks import *

def markdown_to_html_node(markdown):
    # split into blocks
    blocks = markdown_to_blocks(markdown)
    blocks_list = []
    debug_print(blocks)
    # loop over blocks
    for block in blocks:
        # determine type of block
        print(f"block: {block}")
        block_types = block_to_block_types(block)
        print(f"block_types: {block_types}")
        debug_print(block_types)
        convert = ()
        # create new html nodes with proper data
        # for block_type in block_types:
        #     html_nodes = markdown_to_html_node(block_type)
        # assign child htmlnode objects to block node
    # make all block nodes children  under single parent html node
    return blocks_list

def markdown_blocks_to_html_nodes(html_node, block_type):
    pass