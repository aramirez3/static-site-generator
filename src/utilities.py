import html
from enum import Enum
import re

from leafnode import LeafNode
from textnode import TextNode

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
    if not delimiter:
        return old_nodes
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextTypes.TEXT.value:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown: Unmatched delimiters for {delimiter}")
            
        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextTypes.TEXT.value))
                else:
                    new_nodes.append(TextNode(part, text_type))
    
    for node in new_nodes:
        if node.text_type == TextTypes.CODE.value:
            node.text = html.escape(node.text)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    nodes_list = []
    return nodes_list

def split_nodes_link(old_nodes):
    nodes_list = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links):
            for link in links:
                print(f"::::thelink: {link}::::")
                parts = node.text.split(f"[{link[0]}]({link[1]})")
                if parts:
                    print(f"parts: {parts}")
                    for i, part in enumerate(parts):
                        if i % 2 == 0:
                            nodes_list.append(TextNode(part, TextTypes.TEXT.value))
                        else:
                            nodes_list.append(TextNode(link[0], TextTypes.LINK.value, link[1]))
    print(f"nodes_list: {nodes_list}")                            
    return nodes_list