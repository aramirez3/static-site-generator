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
    
def debug_print(the_string):
    print("\n:::::::::::")
    print(the_string)