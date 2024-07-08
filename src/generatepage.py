from markdown_blocks import markdown_to_html_node
import os

def generate_title(markdown):
    # Separate markdown blocks to iterate through and find '#' and extract the title
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Invlaid markdown syntax, no h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    #open source file and assign it to a variable
    file = open(from_path, "r")
    markdown = file.read()
    file.close()

    #open template file and assign it to a variable
    file = open(template_path, "r")
    template = file.read()
    file.close()

    #convert markdown to html nodes and assign raw html nodes to variable
    html = markdown_to_html_node(markdown).to_html()
    title = generate_title(markdown)

    #Use template to complete raw html for full web page
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    #get full destination path, create destination file if it doesn't exist and write full html to it
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def generate_pages_rec(dir_path_content, template_path, dest_dir_path):
    #ensure desination path exists
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok = True)
    #iterate through each item in source directory, if it's a markdown file convert it to an html file
    for item in os.listdir(dir_path_content):
        if os.path.isfile(f"{dir_path_content}/{item}"):
            if ".md" in item:
                #assign raw markdown to a variable
                file = open(os.path.join(dir_path_content, item), "r")
                markdown = file.read()
                file.close()

                #assign template html to variable
                file = open(template_path, "r")
                template = file.read()
                file.close()

                #create html nodes from markdown and create complete html variable with html nodes and template html
                html = markdown_to_html_node(markdown).to_html()
                title = generate_title(markdown)
                template = template.replace("{{ Title }}", title)
                template = template.replace("{{ Content }}", html)

                #write complete raw html to destination file path
                dest_file = f"{item.split(".")[0]}.html"
                to_file = open(os.path.join(dest_dir_path, dest_file), "w")
                to_file.write(template)
                to_file.close()
        else:
            #if item is a directory: recurse using new directory as source
            generate_pages_rec(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item.split(".")[0]))   