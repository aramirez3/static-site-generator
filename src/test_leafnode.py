from assertionhelper import AssertionHelper

from leafnode import LeafNode

class TestLeafNode(AssertionHelper):
    def test_default_values(self):
        node = LeafNode('p', 'Best paragraph ever!', {"class":"p-4 my-8"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Best paragraph ever!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'class':'p-4 my-8'})
        
    def test_repr(self):
        node = LeafNode('p', 'Best paragraph ever!', {"class":"p-4 my-8"})
        self.assertEqual(repr(node), "LeafNode(p, Best paragraph ever!, {'class': 'p-4 my-8'})")
        
    def test_to_html_no_tag_provided(self):
        node = LeafNode(None, 'This should return a raw string', {"class":"green"})
        self.assertEqual(node.to_html(), 'This should return a raw string')
        
    def test_to_html(self):
        node = LeafNode('p', 'Best paragraph ever!', {"class":"p-4 my-8", "target": "_blank"})
        self.assertEqual(node.to_html(), "<p class=\"p-4 my-8\" target=\"_blank\">Best paragraph ever!</p>")

    def test_to_html_no_value(self):
        node = LeafNode('p', None, {"class":"red"})
        self.assert_exception_and_message(node.to_html, ValueError, "Leaf node must contain a value")
        
        
if __name__ == "__main__":
    AssertionHelper.main()