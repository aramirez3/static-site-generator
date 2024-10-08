from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import text_node_to_html_node


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
            {"text":"text type", "text_type": "text", "url": None, "expected": {
                "tag": "", "value": "text type", "props": None
            }},
            {"text":"bold type", "text_type": "bold", "url": None, "expected": {
                "tag": "b", "value": "bold type", "props": None
            }},
            {"text":"italic type", "text_type": "italic", "url": None, "expected": {
                "tag": "i", "value": "italic type", "props": None
            }},
            {"text":"code type", "text_type": "code", "url": None, "expected": {
                "tag": "code", "value": "code type", "props": None
            }},
            {"text":"link type", "text_type": "link", "url": "/home", "expected": {
                "tag": "a", "value": "link type", "props": {'href': '/home'}
            }},
            {"text":"image type", "text_type": "image", "url": "/images/doggie.jpg", "expected": {
                "tag": "img", "value": "", "props": {'src': '/images/doggie.jpg', 'alt': 'image type'}
            }}
        ]
        for item in list_of_types:
            text = TextNode(item["text"], item["text_type"], item["url"])
            leaf = text_node_to_html_node(text)
            self.text_type_conversion_assertions(leaf, item["expected"]["tag"], item["expected"]["value"], item["expected"]["props"])
    
    def test_text_types_not_valid(self):
        node = TextNode("invalid type", "boomerang")
        self.assert_exception_and_message(text_node_to_html_node, ValueError, "Not a valid text type", node)
    
    def text_type_conversion_assertions(self, node, tag, value, props = None):
        print(f'node being tested: {node}')
        self.assertEqual(type(node).__name__, "LeafNode")
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.props, props)
        
if __name__ == "__main__":
    AssertionHelper.main()