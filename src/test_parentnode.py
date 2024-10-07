import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_default_values(self):
        node = ParentNode('p', [], {"class":"all-of-them"})
        self.assertEqual(node.tag, 'p')
        self.value(node.tag, 'p')
        self.children(node.tag, 'p')
        self.props(node.tag, 'p')