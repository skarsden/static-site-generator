
from copystatic import copy_static
from generatepage import generate_pages_rec
import os
import shutil

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_static("./static", "./public")
    generate_pages_rec("./content", "./template.html", "./public")

main()