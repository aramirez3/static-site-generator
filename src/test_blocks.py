from blocks import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


class TestTextNode(AssertionHelper):
    def test_markdown_to_blocks(self):
        text = """
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
        expected = []
        self.assertEqual(actual, expected)
        
    def test_markdown_to_blocks_trim_whitespace(self):
        markdown_text="""
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        
        actual = markdown_to_blocks(markdown_text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_headings(self):
        for i in range(1,7):
            text = f"{i * '#'} This is a heading"
            expected = BlockTypes.HEADING.value
            actual = block_to_block_types(text)
            self.assertEqual(actual, expected)
            
    def test_md_blocks_code(self):
        text = "```print('Hello world')```"
        expected = BlockTypes.CODE.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_quote(self):
        text = "> To be or not to be"
        expected = BlockTypes.QUOTE.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_unordered_list_asterisk(self):
        text = """* first item
* second item
* third item"""
        expected = BlockTypes.UNORDERED_LIST.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_unordered_list_hyphen(self):
        text = """- first item
- second item
- third item"""
        expected = BlockTypes.UNORDERED_LIST.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_ordered_list(self):
        text = """1. first item
2. second item
3. third item"""
        expected = BlockTypes.ORDERED_LIST.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_paragraph(self):
        text = "The quick brown fox jumped over the lazy dog."
        expected = BlockTypes.PARAGRAPH.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    AssertionHelper.main()