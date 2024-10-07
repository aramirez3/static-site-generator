import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()