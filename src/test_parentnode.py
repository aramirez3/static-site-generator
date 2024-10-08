from assertionhelper import AssertionHelper

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(AssertionHelper):
    def test_repr(self):
        node = ParentNode('p', ['a'], {"class":"all-of-them"})
        self.assertEqual(repr(node), "ParentNode(p, ['a'], {'class': 'all-of-them'})")
    
    def test_default_values(self):
        node = ParentNode('p', ['a'], {"class":"all-of-them"})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, ['a'])
        self.assertEqual(node.props, {'class':'all-of-them'})
        
    def test_to_html_children_empty_list(self):
        node = ParentNode('p', [], {"class":"all-of-them"})
        self.assert_exception_and_message(node.to_html, ValueError, "Parent.children is required")
        
    def test_to_html_children_none(self):
        node = ParentNode('p', None, {"class":"all-of-them"})
        self.assert_exception_and_message(node.to_html, ValueError, "Parent.children is required")
        
    def test_to_html_no_tag(self):
        node = ParentNode(None, ['td', 'td'], {"class":"row"})
        self.assert_exception_and_message(node.to_html, ValueError, "Parent node must have a tag")
        
    def test_to_html(self):
        child1 = LeafNode('p', 'This is a paragraph')
        node = ParentNode('section', [child1], {"class":"content"})
        self.assertEqual(node.to_html(), '<section class="content"><p>This is a paragraph</p></section>')
        

if __name__ == "__main__":
    AssertionHelper.main()