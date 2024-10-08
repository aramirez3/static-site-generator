from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.children is None or self.children == []:
            raise ValueError("Parent.children is required")
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        html_out = "".join(list(map(lambda x: f"<{self.tag}>{x.children.to_html()}</{self.tag}>", self.children)))
        print(html_out())