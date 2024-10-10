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
    
def debug_print(the_string):
    print("\n:::::::::::")
    print(the_string)