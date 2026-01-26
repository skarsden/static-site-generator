import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):
    #HTML Node Tests---------------------------------------------------------------------------------
    def test_node(self):
        node = HTMLNode(tag="header", value="This is a header", children=[], props={})
        self.assertEqual(node.tag, "header")
        self.assertEqual(node.value, "This is a header")
        self.assertNotEqual(node.children, None)
        self.assertNotEqual(node.props, None)
    
    def test_children(self):
        node = HTMLNode(children=[HTMLNode(), HTMLNode()])
        self.assertEqual(len(node.children), 2)

    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(len(node.props), 2)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    #Leaf Node Tests---------------------------------------------------------------------------------
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Here</a>")

    #Parent Node Tests-------------------------------------------------------------------------------
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("p", "child 2")
        child_node3 = LeafNode("a", "child 3", {"href": "https://www.child3.com"})
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span><p>child 2</p><a href=\"https://www.child3.com\">child 3</a></div>"
            )
        
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>"
        )