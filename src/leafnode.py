from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must contain a value")
        if self.tag is None or self.tag == "":
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"