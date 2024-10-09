from blocks import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


class TestTextNode(AssertionHelper):
    def test_markdown_to_blocks(self):
        text = markdown_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        actual = markdown_to_blocks(text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(actual, expected)
        
    def test_markdown_to_blocks_empty(self):
        actual = markdown_to_blocks("")
        expected = ""
        self.assertEqual(actual, expected)
        
        actual = markdown_to_blocks(None)
        expected = None
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    AssertionHelper.main()