from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.children is None or self.children == []:
            raise ValueError("Parent.children is required")
        