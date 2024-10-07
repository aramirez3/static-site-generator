import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_default_values(self):
        node = ParentNode('p', [], {"class":"all-of-them"})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class':'all-of-them'})