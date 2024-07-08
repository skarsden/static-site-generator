from htmlnode import ParentNode
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node

#different markdown types as variables
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

#breaks down mardkdown into distinct blocks
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            blocks.remove(block)
            continue
        block.strip()
    return blocks

#Examines a markdown block and return what type of block it is
def block_to_block_type(block):
    lines = block.split("\n")

    if (block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")):
            return block_type_heading
    
    if len(lines) >= 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code

    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith("> "):
                return block_type_paragraph
        return block_type_quote
            
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
            
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
            
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    
    return block_type_paragraph

#returns html nodes made from text nodes
def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for node in text_nodes:
        htmlnode = text_node_to_html_node(node)
        children.append(htmlnode)
    return children

#returns html header from markdown header
def heading_block_to_html_node(block):
    if block.startswith("# "):
        text = block.lstrip("# ")
        level = 1
    elif block.startswith("## "):
        text = block.lstrip("# ")
        level = 2
    elif block.startswith("### "):
        text = block.lstrip("# ")
        level = 3
    elif block.startswith("#### "):
        text = block.lstrip("# ")
        level = 4
    elif block.startswith("##### "):
        text = block.lstrip("# ")
        level = 5
    elif block.startswith("###### "):
        text = block.lstrip("# ")
        level = 6
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)    
    
#returns html code tags from markdown blocks
def code_block_to_html_node(block):
    text = block.strip("``` ")
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

#returns html quote tags from markdown quote blocks
def quote_block_to_html_node(block):
    md_quotes = block.split("\n")
    strings = []
    for quote in md_quotes:
        strings.append(quote.lstrip("> "))
    text = " ".join(strings)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

#returns html unordered list from markdown unordered list
def ulist_block_to_html_node(block):
    parent_node = ParentNode("ul", [])
    lines = block.split("\n")
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        parent_node.children.append(ParentNode("li", children))
    return parent_node

#returns html ordered list from markdown ordered list
def olist_block_to_html_node(block):
    parent_node = ParentNode("ol", [])
    lines = block.split("\n")
    i = 1
    for line in lines:
        text = line.lstrip(f"{i}. ")
        children = text_to_children(text)
        parent_node.children.append(ParentNode("li", children))
        i += 1
    return parent_node

#return html paragraph from markdown paragraph
def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

#creates html nodes from markdown blocks
def markdown_to_html_node(markdown):
    root_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            node = heading_block_to_html_node(block)
        elif block_to_block_type(block) == block_type_code:
            node = code_block_to_html_node(block)
        elif block_to_block_type(block) == block_type_quote:
            node = quote_block_to_html_node(block)
        elif block_to_block_type(block) == block_type_unordered_list:
            node = ulist_block_to_html_node(block)
        elif block_to_block_type(block) == block_type_ordered_list:
            node = olist_block_to_html_node(block)
        elif block_to_block_type(block) == block_type_paragraph:
            node = paragraph_block_to_html_node(block)
        root_node.children.append(node)
    return root_node
