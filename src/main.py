from markdown_blocks import markdown_to_html_node

def main():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    nodes = markdown_to_html_node(md)
    for node in nodes:
        print(node.to_html())
main()