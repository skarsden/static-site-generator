class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("To be overriden")
    
    def props_to_html(self):
        props_html = ""
        if self.props is None or len(self.props) == 0:
            return props_html
        for prop in self.props:
            props_html += f"{prop}=\"{self.props[prop]}\" "
        return props_html.rstrip()
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProperties: {self.props_to_html()}"