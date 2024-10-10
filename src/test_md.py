from md import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


class TestTextNode(AssertionHelper):
    br = "\n\n"
    h1 = "# Hello world"
    h2 = "## h2"
    
    def test_md(self):
        md_block = "".join([self.h1, self.br, self.h2])
        actual = markdown_to_html_node(md_block)
        expected = "<h1>Hello world</h1>"
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    AssertionHelper.main()