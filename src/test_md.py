from md import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from md import *
from utilities import *
from htmlnode import HTMLNode


class TestTextNode(AssertionHelper):
    def test_md(self):
        actual = markdown_to_html_node("# h1 heading")
        expected = []
        html_node = HTMLNode("h1", "h1 heading")
        expected.append(html_node)
        print("")
        print(f"value: {actual[0].value == html_node.value}")
        print(f"tag: {actual[0].tag == html_node.tag}")
        print(f"children: {actual[0].children == html_node.children}")
        print(f"props: {actual[0].props == html_node.props}")
        print(f"object: {actual[0] == html_node}")
        print(f"type: {type(actual[0]) == type(html_node)}")
        print(f"{actual[0]} -- {html_node}")
        self.assertEqual(actual[0], expected)
    
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