import shutil
import os
from markdown_blocks import extract_title, markdown_to_html_node

def copy_static(src, dest):
    if dest == "./public":
        shutil.rmtree(dest)
        os.mkdir("./public")
    for item in os.listdir(src):
        file_path = os.path.join(src, item)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)
        else:
            new_src = os.path.join(src, item)
            new_dest = os.path.join(dest, item)
            os.mkdir(new_dest)
            copy_static(new_src, new_dest)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = ""
    template = ""
    html = ""
    with open(from_path) as file:
        md = file.read()
    with open(template_path) as file:
        template = file.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md).lstrip("# ")
    web_page = template.replace("{{ Title }}", title)
    web_page = web_page.replace("{{ Content }}", html)

    with open(dest_path, "x") as file:
        file.write(web_page)
    

def main():
    copy_static("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()