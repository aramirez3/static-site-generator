from assertionhelper import AssertionHelper
from os import path

from template import *
from md_blocks import markdown_to_html_node

class TestParentNode(AssertionHelper):
    def test_extract_title(self):
        text = """# This is a test

This is only a test.
"""
        title = extract_title(text)
        self.assertEqual(title, "This is a test")
        
        text2 = "# Simple test"
        title2 = extract_title(text2)
        self.assertEqual(title2, "Simple test")
    
    def test_extract_title_none_provided(self):
        text = "Title with no # provided"
        expected = "Title (h1) is required"
        self.assert_exception_and_message(extract_title, ValueError, expected, text)
        
        
if __name__ == "__main__":
    AssertionHelper.main()
