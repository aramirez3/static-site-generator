from md_blocks import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from parentnode import ParentNode
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
        
    def test_block_to_block_type(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_types(block), BlockTypes.PARAGRAPH.value)
        block = "# This is an h1"
        self.assertEqual(block_to_block_types(block), BlockTypes.HEADING.value)
        block = "> This is a quote"
        self.assertEqual(block_to_block_types(block), BlockTypes.QUOTE.value)
        block = "* this is an unordered list"
        self.assertEqual(block_to_block_types(block), BlockTypes.UNORDERED_LIST.value)
        block = "- this is an unordered list"
        self.assertEqual(block_to_block_types(block), BlockTypes.UNORDERED_LIST.value)
        block = "1. this is an ordered list"
        self.assertEqual(block_to_block_types(block), BlockTypes.ORDERED_LIST.value)
        block = "```\nThis is code\n```"
        self.assertEqual(block_to_block_types(block), BlockTypes.CODE.value)
        
    def test_block_to_paragraph_node(self):
        markdown = "Regular paragraph. With some **bold** text."
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        self.assertEqual(html, "<div><p>Regular paragraph. With some <b>bold</b> text.</p></div>")
        
    def test_block_to_html_node(self):
        markdown = """# How to write markdown

Go to the googles. Search for chat gippity.

Ask gippity to google for you."""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        self.assertEqual(html, "<div><h1>How to write markdown</h1><p>Go to the googles. Search for chat gippity.</p><p>Ask gippity to google for you.</p></div>")
        
    def test_block_to_quote_node(self):
        markdown = "> Don't quote me"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
    
    def test_block_to_code_node(self):
        markdown = """## How to Python
        
```print('hello world')```

BOOM. Done.
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        print(html)
    
    
if __name__ == "__main__":
    AssertionHelper.main()