from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        
    def to_html(self):
        if self.children is None or self.children == []:
            raise ValueError("Parent.children is required")
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"