class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("To be overriden by child classes")
    
    #Converts properties to html property syntax
    def props_to_html(self):
        prop_string = ""
        for prop in self.props:
            prop_string += f" {prop}=\"{self.props[prop]}\""
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode:\ntag = {self.tag}\nvalue = {self.value}\nprops = {self.props}\nChildren = {self.children}\n"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    #returns Leaf Node as raw html
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must contain a value")
        elif self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props = self.props_to_html()
                return f"<{self.tag}{props}>{self.value}</{self.tag}>"
            
    def __repr__(self):
        return f"LeafNode: tag = {self.tag}, value = {self.value}, props = {self.props}"
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = ""):
        super().__init__(tag, None, children, props)
    
    #returns Parent Node as raw html
    def to_html(self):
        if self.tag == "":
            raise ValueError("No tags provided")
        if self.children == []:
            raise ValueError("No children provided")
        
        text_tree = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            text_tree += child.to_html()
        return text_tree + f"</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode:\ntag = {self.tag}\nvalue = {self.value}\nprops = {self.props}\nChildren = {self.children}"