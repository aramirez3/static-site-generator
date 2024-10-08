from leafnode import LeafNode
from enum import Enum

class TextTypes(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextTypes.TEXT:
        return LeafNode("", text_node.text)
    elif text_node.text_type == TextTypes.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextTypes.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextTypes.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextTypes.LINK:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == TextTypes.IMAGE:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        print(f"\nnode type: {text_node.text_type}")
        raise ValueError("Not a valid text type")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    pass