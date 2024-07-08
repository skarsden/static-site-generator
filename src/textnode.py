from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        if self.url != None:
            return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"
        else:
            return f"TextNode(\"{self.text}\", {self.text_type})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"text_node.text"})
    else:
        raise Exception("Invalid Text Type")
