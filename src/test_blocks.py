from md_blocks import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


class TestTextNode(AssertionHelper):
    def test_markdown_to_blocks(self):
        text = """\n# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"""
        actual = markdown_to_blocks(text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
        ]
        self.assertEqual(actual, expected)
        
    def test_markdown_to_blocks_code(self):
        actual = markdown_to_blocks("```print('hello world')```")
        expected = ["```print('hello world')```"]
        self.assertEqual(actual, expected)
        
    def test_markdown_to_blocks_empty(self):
        actual = markdown_to_blocks("")
        expected = []
        self.assertEqual(actual, expected)
        
    def test_markdown_to_blocks_trim_whitespace(self):
        markdown_text="""\nThis is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"""
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
        text = "```\nprint('Hello world')\n```"
        expected = BlockTypes.CODE.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_quote(self):
        text = "> To be or not to be"
        expected = BlockTypes.QUOTE.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_unordered_list_asterisk(self):
        text = """* first item\n* second item\n* third item"""
        expected = BlockTypes.UNORDERED_LIST.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_unordered_list_hyphen(self):
        text = """- first item\n- second item\n- third item"""
        expected = BlockTypes.UNORDERED_LIST.value
        actual = block_to_block_types(text)
        self.assertEqual(actual, expected)
        
    def test_md_blocks_ordered_list(self):
        text = """1. first item\n2. second item\n3. third item"""
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