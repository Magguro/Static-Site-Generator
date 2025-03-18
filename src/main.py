import os
import shutil
import sys
from markdown_blocks import markdown_to_html_node, extract_title
from pathlib import Path


def copy_static(source_dir, dest_dir):
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Create destination directory
    os.mkdir(dest_dir)

    # Get all files and directories in source
    items = os.listdir(source_dir)

    # Iterate through all items
    for item in items:
        # Create full paths
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        # Check if it's a file or directory
        if os.path.isfile(source_item):
            # It's a file - copy it
            print(f"Copying file: {source_item} to {dest_item}")
            shutil.copy(source_item, dest_item)
        else:
            # It's a directory - recursively copy it
            print(f"Copying directory: {source_item} to {dest_item}")
            copy_static(source_item, dest_item)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    # Read template content
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title from markdown
    title = extract_title(markdown_content)

    # Replace placeholders in template
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    # Update paths with basepath
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write to destination file
    with open(dest_path, 'w') as f:
        f.write(full_html)

def generate_pages_recursive(content_dir, template_path, output_dir, basepath):
    """
    Recursively generates pages from content directory
    """
    content_path = Path(content_dir)
    for item in content_path.iterdir():  # This returns Path objects, not strings
        if item.is_file():
            if item.suffix == ".md":
                generate_page(
                    from_path=item,
                    template_path=template_path,
                    dest_path=os.path.join(output_dir, item.name.replace(".md", ".html")),
                    basepath=basepath
                )
        elif item.is_dir():
            new_content_dir = str(item)
            new_output_dir = os.path.join(output_dir, item.name)
            os.makedirs(new_output_dir, exist_ok=True)
            generate_pages_recursive(new_content_dir, template_path, new_output_dir, basepath)

def main():
    # Get basepath from command line or use default
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Ensure basepath doesn't end with a slash unless it's the root
    # if basepath != "/" and basepath.endswith("/"):
    #     basepath = basepath[:-1]

    print(f"Using basepath: {basepath}")

    # Delete and recreate the public directory
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs")

    # Copy all static files
    if os.path.exists("static"):
        copy_static("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
