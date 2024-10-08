import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_default_values(self):
        node = ParentNode('p', ['a'], {"class":"all-of-them"})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, ['a'])
        self.assertEqual(node.props, {'class':'all-of-them'})
        
    def test_to_html_no_children(self):
        node = ParentNode('p', [], {"class":"all-of-them"})
        self.assertRaises(ValueError, node.to_html(), msg="Parent.children is required")
        node2 = ParentNode('p', None, {"class":"all-of-them"})
        self.assertRaises(ValueError, node2.to_html(), msg="Parent.children is required")
        
    def test_to_html_no_tag(self):
        node = ParentNode(None, ['td', 'td'], {"class":"row"})
        self.assertRaises(ValueError, node.to_html(), msg="Parent node must have a tag")
        
    def test_to_html(self):
        child1 = LeafNode('p', 'This is a paragraph')
        child2 = LeafNode('p', 'This is my second paragraph.')
        child3 = LeafNode('p', 'Third???!?!?!?!')
        node = ParentNode('section', [child1, child2, child3], {"class":"content"})
        print(node.to_html)