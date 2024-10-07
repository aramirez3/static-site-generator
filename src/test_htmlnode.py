import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_default_values(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_not_implemented_error(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        self.assertRaises(NotImplementedError, node.to_html)
        
    def test_repr(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        assert repr(node) == "HTMLNode('a', 'home', None, {'href': '/'})"
    
    def test_props_to_html(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        expected = ' href="/"'
        self.assertEqual(node.props_to_html(), expected)
        

if __name__ == "__main__":
    unittest.main()