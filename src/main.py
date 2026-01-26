from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    node = LeafNode(tag="p", value="This is some anchor text")
    node2 = LeafNode(tag="a", value="Click Here", props={"href": "https://www.google.com"})
    print(node.to_html())
    print(node2.to_html())

main()