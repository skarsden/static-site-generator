import re
from textnode import (TextNode, text_type_text, text_type_image, text_type_link, text_type_bold, text_type_code, text_type_italic)

#Breaks down text into text nodes based on contents of text
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        strings = node.text.split(delimiter)
        if len(strings) % 2 == 0:
             raise ValueError("Invalid sytnax, no closing delimiter found.")
        for i in range(len(strings)):
            if strings[i] == "":
                    continue
            if i % 2 == 0:
                split_nodes.append(TextNode(strings[i], text_type_text))
            else:
                split_nodes.append(TextNode(strings[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

#retrieve image link from text
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

#retrieve web link from text
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

# get images from text
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        #set text to pull image from
        original_text = node.text
        images = extract_markdown_images(original_text)
        #if there's no image: check next part of text
        if len(images) == 0:
            new_nodes.append(node)
            continue
        #if image is found: check for valid syntax and append image and surrounding text to new nodes
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid syntax, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

#get link from text
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        #text to pull link from
        original_text = node.text
        links = extract_markdown_links(original_text)
        #if no links are found: check next part of text
        if len(links) == 0:
            new_nodes.append(node)
            continue
        #If link is found: check for valid syntax and append link and surrounding text to new nodes
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid syntax, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
    
#gets text nodes with appropriate text types from text and returns node list
def text_to_text_nodes(text):
    text_nodes = [TextNode(text, text_type_text)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes


