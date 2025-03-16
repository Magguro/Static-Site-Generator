import os
import shutil
from markdown_blocks import markdown_to_html_node, extract_title


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

def generate_page(from_path, template_path, dest_path):
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

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write to destination file
    with open(dest_path, 'w') as f:
        f.write(full_html)

def main():
    # Delete and recreate the public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")

    # Copy all static files
    if os.path.exists("static"):
        copy_static("static", "public")

    # Generate the index page
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html"
    )

main()
