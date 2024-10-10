import html
from enum import Enum
import re

from leafnode import LeafNode
from textnode import TextNode

regex_values = {
    "heading": r"(\#{1,6})",
    "code": r"^(\`{3}).*\`{3}",
    "quote": r"^(\>{1}.*)",
    "unordered_list": r"(\-|\*)\s",
    "ordered_list": "working on this piece"
}

class TextTypes(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class Delimiters(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"
    
class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def get_block_tags():
    return {
        "paragraph": "p",
        "heading": {
            "h1": "h1",
            "h2": "h2",
            "h3": "h3",
            "h4": "h4",
            "h5": "h5",
            "h6": "h6",
        },
        "code": "pre",
        "quote": "blockquote",
        "unordered_list": "li",
        "ordered_list": "ol",
    }
    
def debug_print(the_string):
    print("\n:::::::::::")
    print(the_string)
    print("\n:::::::::::")
    
def regex_match(regex, text):
    return re.match(regex, text)