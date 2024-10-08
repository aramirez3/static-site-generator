from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


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
        
    def test_split_nodes_delimiter(self):
        code = TextNode("This is text with a `code block` word", TextTypes.TEXT.value)
        new_code = split_nodes_delimiter([code], "`", TextTypes.CODE.value)
        expected_code = [
            TextNode("This is text with a ", TextTypes.TEXT.value, None),
            TextNode("code block", TextTypes.CODE.value, None),
            TextNode(" word", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_code, expected_code)
        
        bold = TextNode("Text with one **bold** word", TextTypes.TEXT.value)
        new_bold = split_nodes_delimiter([bold], "**", TextTypes.BOLD.value)
        expected_bold = [
            TextNode("Text with one ", TextTypes.TEXT.value, None),
            TextNode("bold", TextTypes.BOLD.value, None),
            TextNode(" word", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_bold, expected_bold)
        
        italic = TextNode("Text with *italicized words* bruh.", TextTypes.TEXT.value)
        new_italic = split_nodes_delimiter([italic], "*", TextTypes.ITALIC.value)
        expected_italic = [
            TextNode("Text with ", TextTypes.TEXT.value, None),
            TextNode("italicized words", TextTypes.ITALIC.value, None),
            TextNode(" bruh.", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_italic, expected_italic)
    
    def test_split_nodes_delimiter_multiple(self):
        italic = TextNode("Text with *italicized words* multiple *times*.", TextTypes.TEXT.value)
        new_italic = split_nodes_delimiter([italic], "*", TextTypes.ITALIC.value)
        expected_italic = [
            TextNode("Text with ", TextTypes.TEXT.value, None),
            TextNode("italicized words", TextTypes.ITALIC.value, None),
            TextNode(" multiple ", TextTypes.TEXT.value, None),
            TextNode("times", TextTypes.ITALIC.value, None),
            TextNode(".", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_italic, expected_italic)
    
    def test_split_nodes_delimiter_edge_cases(self):
        node = TextNode("No delimiters", TextTypes.TEXT.value)
        new_node = split_nodes_delimiter([node], "", TextTypes.TEXT.value)
        self.assertEqual(new_node, [TextNode("No delimiters", TextTypes.TEXT.value, None)])
        
        node= TextNode("", TextTypes.TEXT.value)
        new_nodes = split_nodes_delimiter([node], "*", TextTypes.ITALIC.value)
        self.assertEqual(new_nodes, [])
        
        
        node= TextNode('Code with special chars: `"$url" =~ ^https?://([^/]+)`', TextTypes.TEXT.value)
        new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE.value)
        expected = [
            TextNode('Code with special chars: ', TextTypes.TEXT.value, None),
            TextNode('&quot;$url&quot; =~ ^https?://([^/]+)', TextTypes.CODE.value, None),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_extract_markdown_images(self):
        text = "Text with a ![Ricky R](https://i.imgur.com/aKaOqIh.gif) and ![obi juan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        expected = [('Ricky R', 'https://i.imgur.com/aKaOqIh.gif'), ('obi juan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(images, expected)
        
    def test_extract_markdown_links(self):
        text = "Text with a link [to YouTube](https://youtu.be)"
        links = extract_markdown_links(text)
        expected = [('to YouTube', 'https://youtu.be')]
        self.assertEqual(links, expected)
    
if __name__ == "__main__":
    AssertionHelper.main()