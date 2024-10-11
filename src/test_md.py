from md import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from md import *
from utilities import *
from htmlnode import HTMLNode


class TestTextNode(AssertionHelper):
    def test_md_paragraph(self):
        node_list = markdown_to_html_node("# h1 heading")
        node = node_list[0]
        self.assertEqual(type(node_list).__name__, "list")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "h1 heading")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_md_heading(self):
        node_list = markdown_to_html_node("Basic paragraph.\nThis\nshould\nbe\none\nnode")
        node = node_list[0]
        self.assertEqual(type(node_list).__name__, "list")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Basic paragraph.\nThis\nshould\nbe\none\nnode")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_md_quote(self):
        node_list = markdown_to_html_node("> Win Forever")
        node = node_list[0]
        self.assertEqual(type(node_list).__name__, "list")
        self.assertEqual(node.tag, "blockquote")
        self.assertEqual(node.value, "Win Forever")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_md_code(self):
        node_list = markdown_to_html_node("```print('hello world')\n\n# hello world```")
        print(node_list)
        node = node_list[0]
        self.assertEqual(type(node_list).__name__, "list")
        self.assertEqual(node.tag, "pre")
        self.assertEqual(node.value, "print('hello world')\n\n# hello world")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    # def test_get_block_text_heading(self):
    #     actual = get_block_text("### h3 heading", BlockTypes.HEADING.value)
    #     expected = "h3 heading"
    #     self.assertEqual(actual, expected)
        
    # def test_get_block_text_paragraph(self):
    #     actual = get_block_text("Just a normal paragraph", BlockTypes.PARAGRAPH.value)
    #     expected = "Just a normal paragraph"
    #     self.assertEqual(actual, expected)
        
        ### delete
        
        
    # def test_remove_leading_chars_single_line(self):
    #     text = "## h2 heading"
    #     actual = remove_leading_chars_single_line(text, regex_values[BlockTypes.HEADING.value])
    #     expected = "h2 heading"
    #     self.assertEqual(actual, expected)
        
    # def test_remove_leading_chars_ul_asterisk(self):
    #     text = "* first\n* second\n* third"
    #     actual = remove_leading_chars_list(text, BlockTypes.UNORDERED_LIST.value)
    #     expected = "first\nsecond\nthird"
    #     self.assertEqual(actual, expected)
        
    # def test_remove_leading_chars_ul_dash(self):
    #     text = "- first\n- second\n- third"
    #     actual = remove_leading_chars_list(text, BlockTypes.UNORDERED_LIST.value)
    #     expected = "first\nsecond\nthird"
    #     self.assertEqual(actual, expected)
        
    # def test_remove_leading_chars_ol(self):
    #     text = "1. first\n2. second\n3. third"
    #     actual = remove_leading_chars_list(text, BlockTypes.ORDERED_LIST.value)
    #     expected = "first\nsecond\nthird"
    #     self.assertEqual(actual, expected)
        
    # def test_remove_leading_chars_code(self):
    #     text = "```print('hello world')\n\n# hello world```"
    #     actual = remove_leading_chars_code(text)
    #     expected = "print('hello world')\n\n# hello world"
    #     self.assertEqual(actual, expected)
        
    # def test_remove_leading_chars_quote(self):
    #     text = "> Job's not finished"
    #     actual = remove_leading_chars_single_line(text, r"(\>\s)")
    #     expected = "Job's not finished"
    #     print(f"actual: {actual}")
    #     print(f"expected: {expected}")
    #     self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    AssertionHelper.main()