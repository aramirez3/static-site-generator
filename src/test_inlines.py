from md_inlines import *

from unittest.result import TestResult
from assertionhelper import AssertionHelper

from textnode import TextNode
from utilities import *


class TestTextNode(AssertionHelper):
        
    def test_split_nodes_delimiter_code(self):
        code = TextNode("This is text with a `code block` word", TextTypes.TEXT.value)
        new_code = split_nodes_delimiter([code], Delimiters.CODE.value, TextTypes.CODE.value)
        expected_code = [
            TextNode("This is text with a ", TextTypes.TEXT.value, None),
            TextNode("code block", TextTypes.CODE.value, None),
            TextNode(" word", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_code, expected_code)
    
    def test_split_nodes_delimiter_bold(self):    
        bold = TextNode("Text with one **bold** word", TextTypes.TEXT.value)
        new_bold = split_nodes_delimiter([bold], Delimiters.BOLD.value, TextTypes.BOLD.value)
        expected_bold = [
            TextNode("Text with one ", TextTypes.TEXT.value, None),
            TextNode("bold", TextTypes.BOLD.value, None),
            TextNode(" word", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_bold, expected_bold)
        
    def test_split_nodes_delimiter_italic(self):
        italic = TextNode("Text with *italicized words* bruh.", TextTypes.TEXT.value)
        new_italic = split_nodes_delimiter([italic], Delimiters.ITALIC.value, TextTypes.ITALIC.value)
        expected_italic = [
            TextNode("Text with ", TextTypes.TEXT.value, None),
            TextNode("italicized words", TextTypes.ITALIC.value, None),
            TextNode(" bruh.", TextTypes.TEXT.value, None),
        ]
        self.assertEqual(new_italic, expected_italic)
    
    def test_split_nodes_delimiter_multiple(self):
        italic = TextNode("Text with *italicized words* multiple *times*.", TextTypes.TEXT.value)
        new_italic = split_nodes_delimiter([italic], Delimiters.ITALIC.value, TextTypes.ITALIC.value)
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
        new_node = split_nodes_delimiter([node], Delimiters.TEXT.value, TextTypes.TEXT.value)
        self.assertEqual(new_node, [TextNode("No delimiters", TextTypes.TEXT.value, None)])
        
        node= TextNode("", TextTypes.TEXT.value)
        new_nodes = split_nodes_delimiter([node], Delimiters.ITALIC.value, TextTypes.ITALIC.value)
        self.assertEqual(new_nodes, [])
        
        
        node= TextNode('Code with special chars: `"$url" =~ ^https?://([^/]+)`', TextTypes.TEXT.value)
        new_nodes = split_nodes_delimiter([node], Delimiters.CODE.value, TextTypes.CODE.value)
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
        
    def test_split_nodes_image(self):
        node = TextNode("Text with a ![Ricky R](https://i.imgur.com/aKaOqIh.gif) and ![obi juan](https://i.imgur.com/fJRm4Vk.jpeg)", TextTypes.TEXT.value)
        node_list = split_nodes_image([node])
        expected = [
            TextNode("Text with a ", TextTypes.TEXT.value, None),
            TextNode("Ricky R", TextTypes.IMAGE.value, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextTypes.TEXT.value, None),
            TextNode("obi juan", TextTypes.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(node_list, expected)
        
    def test_split_nodes_link(self):
        node1 = TextNode("Text with a link [to YouTube](https://youtu.be). Sweet", TextTypes.TEXT.value)
        node1_list = split_nodes_link([node1])
        expected1 = [
            TextNode("Text with a link ", TextTypes.TEXT.value, None),
            TextNode("to YouTube", TextTypes.LINK.value, "https://youtu.be"),
            TextNode(". Sweet", TextTypes.TEXT.value, None)
        ]
        self.assertEqual(node1_list, expected1)
        
        node2 = TextNode("Two nodes [with link](http://localhost)", TextTypes.TEXT.value)
        node2_list = split_nodes_link([node2])
        expected2 = [
            TextNode("Two nodes ", TextTypes.TEXT.value, None),
            TextNode("with link", TextTypes.LINK.value, "http://localhost"),
        ]
        self.assertEqual(node2_list, expected2)
        
    def test_split_nodes_multiple_links(self):
        node = TextNode("Text [with link](http://localhost) with another [link](http://localhost/home)", TextTypes.TEXT.value)
        node_list = split_nodes_link([node])
        expected = [
            TextNode("Text ", TextTypes.TEXT.value, None),
            TextNode("with link", TextTypes.LINK.value, "http://localhost"),
            TextNode(" with another ", TextTypes.TEXT.value, None),
            TextNode("link", TextTypes.LINK.value, "http://localhost/home"),
        ]
        self.assertEqual(node_list, expected)
        
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextTypes.TEXT.value),
            TextNode("text", TextTypes.BOLD.value),
            TextNode(" with an ", TextTypes.TEXT.value),
            TextNode("italic", TextTypes.ITALIC.value),
            TextNode(" word and a ", TextTypes.TEXT.value),
            TextNode("code block", TextTypes.CODE.value),
            TextNode(" and an ", TextTypes.TEXT.value),
            TextNode("obi wan image", TextTypes.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextTypes.TEXT.value),
            TextNode("link", TextTypes.LINK.value, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)
        
    def test_text_to_textnodes_invalid(self):
        delims = [
            Delimiters.BOLD,
            Delimiters.ITALIC,
            Delimiters.CODE
        ]
        for delim in delims:
            text = f"Test with {delim.value}unmatched delimiters"
            expected_message = f"Invalid markdown: Unmatched delimiters for {delim.value}"
            self.assert_exception_and_message(text_to_textnodes, ValueError, expected_message, text)
    
    
if __name__ == "__main__":
    AssertionHelper.main()