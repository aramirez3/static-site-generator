from md import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from md import *
from utilities import *
from htmlnode import HTMLNode


class TestTextNode(AssertionHelper):
    def test_md(self):
        actual = markdown_to_html_node("Regular paragraph.\nNew line in same paragraph.")
        expected = []
        html_node = HTMLNode("p", "Regular paragraph.\nNew line in same paragraph.")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_heading(self):
        actual = markdown_to_html_node("# h1 heading")
        expected = []
        html_node = HTMLNode("h1", "h1 heading")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_code(self):
        actual = markdown_to_html_node("```console.log('what')```")
        expected = []
        html_node = HTMLNode("pre", "console.log('what')")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_quote(self):
        actual = markdown_to_html_node("> The Rock says")
        expected = []
        html_node = HTMLNode("blockquote", "The Rock says")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_ul_hyphen(self):
        actual = markdown_to_html_node("- first\n- second\n- third")
        expected = []
        html_node = HTMLNode("blockquote", "first\nsecond\nthird")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_ul_asterisk(self):
        actual = markdown_to_html_node("* first\n* second\n* third")
        expected = []
        html_node = HTMLNode("blockquote", "first\nsecond\nthird")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
        
    def test_md_ol(self):
        actual = markdown_to_html_node("1. first\n2. second\n3. third")
        expected = []
        html_node = HTMLNode("blockquote", "first\nsecond\nthird")
        expected.append(html_node)
        self.assertEqual(actual, [expected])
    
    def test_get_block_text_heading(self):
        actual = get_block_text("### h3 heading", BlockTypes.HEADING.value)
        expected = "h3 heading"
        self.assertEqual(actual, expected)
        
    def test_get_block_text_paragraph(self):
        actual = get_block_text("Just a normal paragraph", BlockTypes.PARAGRAPH.value)
        expected = "Just a normal paragraph"
        self.assertEqual(actual, expected)
        
    def test_remove_leading_chars_single_line(self):
        text = "## h2 heading"
        actual = remove_leading_chars_single_line(text, regex_values[BlockTypes.HEADING.value])
        expected = "h2 heading"
        self.assertEqual(actual, expected)
        
    def test_remove_leading_chars_ul_asterisk(self):
        text = "* first\n* second\n* third"
        actual = remove_leading_chars_list(text, BlockTypes.UNORDERED_LIST.value)
        expected = "first\nsecond\nthird"
        self.assertEqual(actual, expected)
        
    def test_remove_leading_chars_ul_dash(self):
        text = "- first\n- second\n- third"
        actual = remove_leading_chars_list(text, BlockTypes.UNORDERED_LIST.value)
        expected = "first\nsecond\nthird"
        self.assertEqual(actual, expected)
        
    def test_remove_leading_chars_ol(self):
        text = "1. first\n2. second\n3. third"
        actual = remove_leading_chars_list(text, BlockTypes.ORDERED_LIST.value)
        expected = "first\nsecond\nthird"
        self.assertEqual(actual, expected)
        
    def test_remove_leading_chars_code(self):
        text = "```print('hello world')\n\n# hello world```"
        actual = remove_leading_chars_code(text)
        expected = "print('hello world')\n\n# hello world"
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    AssertionHelper.main()