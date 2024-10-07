from  htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        if children is None:
            raise ValueError("children value is required")
        super().__init__(tag, None, children, props)