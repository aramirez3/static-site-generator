from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *
from md_inlines import *


class TestTextNode(AssertionHelper):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "http://0.0.0.0:8888")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, http://0.0.0.0:8888)")
        
    def test_url_default_value(self):
        node = TextNode("This is a text node", "bold")
        assert node.url == None
        
    def test_not_equal_properties(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "header")
        self.assertNotEqual(node, node2)
        
    def test_text_types(self):
        list_of_types = [
            {"text":"text type", "text_type": TextTypes.TEXT.value, "url": None, "expected": {
                "tag": "", "value": "text type", "props": None
            }},
            {"text":"bold type", "text_type": TextTypes.BOLD.value, "url": None, "expected": {
                "tag": "b", "value": "bold type", "props": None
            }},
            {"text":"italic type", "text_type": TextTypes.ITALIC.value, "url": None, "expected": {
                "tag": "i", "value": "italic type", "props": None
            }},
            {"text":"code type", "text_type": TextTypes.CODE.value, "url": None, "expected": {
                "tag": "code", "value": "code type", "props": None
            }},
            {"text":"link type", "text_type": TextTypes.LINK.value, "url": "/home", "expected": {
                "tag": "a", "value": "link type", "props": {'href': '/home'}
            }},
            {"text":"image type", "text_type": TextTypes.IMAGE.value, "url": "/images/doggie.jpg", "expected": {
                "tag": "img", "value": "", "props": {'src': '/images/doggie.jpg', 'alt': 'image type'}
            }}
        ]
        for item in list_of_types:
            text_node = TextNode(item["text"], item["text_type"], item["url"])
            self.text_type_conversion_assertions(text_node, item["expected"]["tag"], item["expected"]["value"], item["expected"]["props"])
    
    def test_text_types_not_valid(self):
        node = TextNode("invalid type", "boomerang")
        self.assert_exception_and_message(text_node_to_html_node, ValueError, "Not a valid text type", node)
        
    def text_type_conversion_assertions(self, text_node, tag, value, props = None):
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(type(leaf_node).__name__, "LeafNode")
        self.assertEqual(leaf_node.tag, tag)
        self.assertEqual(leaf_node.value, value)
        self.assertEqual(leaf_node.props, props)
        
if __name__ == "__main__":
    AssertionHelper.main()