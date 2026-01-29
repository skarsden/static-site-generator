import shutil
import os
import sys
from markdown_blocks import extract_title, markdown_to_html_node

def copy_static(src, dest):
    if dest == "./docs":
        if os.path.exists(dest):
            shutil.rmtree(dest)
        os.mkdir("./docs")
        
    for item in os.listdir(src):
        file_path = os.path.join(src, item)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)
        else:
            new_src = os.path.join(src, item)
            new_dest = os.path.join(dest, item)
            os.mkdir(new_dest)
            copy_static(new_src, new_dest)

def generate_page(from_path, template_path, dest_path, basepath):
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
    web_page = web_page.replace("href=\"/", f"href=\"{basepath}")
    web_page = web_page.replace("src=\"/", f"src=\"{basepath}")

    with open(dest_path, "x") as file:
        file.write(web_page)
    

def generate_pages_recursive(dir_path_content, template_path, dir_path_dest, basepath):
    new_content = ""
    new_dest = ""
    for item in os.listdir(dir_path_content):
        new_content = os.path.join(dir_path_content, item)
        new_dest = os.path.join(dir_path_dest, item)
        if os.path.isfile(new_content):
            generate_page(new_content, template_path, new_dest.replace(".md", ".html"), basepath)
        else:
            os.mkdir(new_dest)
            generate_pages_recursive(new_content, template_path, new_dest, basepath)

def main():
    basepath = "/" if len(sys.argv) == 1 else sys.argv[1]
    copy_static("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()