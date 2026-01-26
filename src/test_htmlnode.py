import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
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