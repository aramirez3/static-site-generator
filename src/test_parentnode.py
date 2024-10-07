import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_default_values(self):
        node = ParentNode('p', ['a'], {"class":"all-of-them"})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, ['a'])
        self.assertEqual(node.props, {'class':'all-of-them'})
        
    def test_to_html_no_children(self):
        node = ParentNode('p', [], {"class":"all-of-them"})
        self.assertRaises(ValueError, node.to_html)
        node2 = ParentNode('p', None, {"class":"all-of-them"})
        self.assertRaises(ValueError, node2.to_html)