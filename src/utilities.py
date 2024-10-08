from leafnode import LeafNode
from textnode import TextNode
from enum import Enum

class TextTypes(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextTypes.TEXT.value:
        return LeafNode("", text_node.text)
    elif text_node.text_type == TextTypes.BOLD.value:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextTypes.ITALIC.value:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextTypes.CODE.value:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextTypes.LINK.value:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == TextTypes.IMAGE.value:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        raise ValueError("Not a valid text type")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if type(node).__name__ != TextNode.__name__:
            new_nodes.append(node)
        elif delimiter in node.text:
            if node.text.count(delimiter) % 2 != 0:
                raise TypeError("Invalid markdown")
            new_list = delimiter_list_builder(node.text.split(delimiter), text_type)
            new_nodes.extend(new_list)
        else:
            new_nodes.append(node)
    return new_nodes

def delimiter_list_builder(strings_list, text_type):
    return_list = []
    inside_delimited_section = False
    for line in strings_list:
        if inside_delimited_section:
            node = TextNode(line, text_type)
            inside_delimited_section = False
        else:
            node = TextNode(line, TextTypes.TEXT.value)
            inside_delimited_section = True
        return_list.append(node)
    return return_list