import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_default_values(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
        node2 = HTMLNode("h1", "The first blog post", None, {"class":"title"})
        self.assertEqual(node2.tag, "h1")
        self.assertEqual(node2.value, "The first blog post")
        self.assertEqual(node2.children, None)
        self.assertEqual(node2.props, {'class':'title'})
    
    def test_not_implemented_error(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        self.assertRaises(NotImplementedError, node.to_html)
        
    def test_repr(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        self.assertEqual(repr(node), "HTMLNode(a, home, children: None, {'href': '/'})")
    
    def test_props_to_html(self):
        node = HTMLNode('a', 'home', None, {"href":"/"})
        self.assertEqual(node.props_to_html(), ' href="/"')
        

if __name__ == "__main__":
    unittest.main()