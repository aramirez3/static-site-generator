import html
import re

from utilities import *
from leafnode import LeafNode
from textnode import TextNode

    
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
    for node in old_nodes:
        if node.text_type != TextTypes.TEXT.value:
            nodes_list.append(node)
            continue
        
        remaining_text = node.text
        images = extract_markdown_images(remaining_text)
        
        if not images:
            nodes_list.append(node)
            continue
        
        start = 0
        for alt_text, image_url in images:
            image_string = f"![{alt_text}]({image_url})"
            image_start = remaining_text.index(image_string, start)
            if image_start > start:
                nodes_list.append(TextNode(remaining_text[start:image_start], TextTypes.TEXT.value))
            nodes_list.append(TextNode(alt_text, TextTypes.IMAGE.value, image_url))
            start = image_start + len(image_string)
            
        if start < len(remaining_text):
            nodes_list.append(TextNode(remaining_text[start:], TextTypes.TEXT.value))
    return nodes_list

def split_nodes_link(old_nodes):
    nodes_list = []
    for node in old_nodes:
        if node.text_type != TextTypes.TEXT.value:
            nodes_list.append(node)
            continue
        
        remaining_text = node.text
        links = extract_markdown_links(remaining_text)
        
        if not links:
            nodes_list.append(node)
            continue
        
        start = 0
        for link_text, link_url in links:
            link_string = f"[{link_text}]({link_url})"
            link_start = remaining_text.index(link_string, start)
            if link_start > start:
                nodes_list.append(TextNode(remaining_text[start:link_start], TextTypes.TEXT.value))
            nodes_list.append(TextNode(link_text, TextTypes.LINK.value, link_url))
            start = link_start + len(link_string)
            
        if start < len(remaining_text):
            nodes_list.append(TextNode(remaining_text[start:], TextTypes.TEXT.value))
    return nodes_list

def text_to_textnodes(text):
    text_node = TextNode(text, TextTypes.TEXT.value)
    # convert text to nodes (string -> list of nodes)
    nodes = split_nodes_delimiter([text_node], Delimiters.BOLD.value, TextTypes.BOLD.value)
    nodes = split_nodes_delimiter(nodes, Delimiters.ITALIC.value, TextTypes.ITALIC.value)
    nodes = split_nodes_delimiter(nodes, Delimiters.CODE.value, TextTypes.CODE.value)
    # split up the link and image nodes
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes