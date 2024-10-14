from md_blocks import markdown_to_html_node

import os

def extract_title(markdown):
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise ValueError("Title (h1) is required")
    else:
        return lines[0].split('# ')[1]
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")
    
    data = ""
    template_data = ""
    
    with open(from_path, "r") as f:
        data = f.read()
        
    with open(template_path, "r") as f:
        template_data = f.read()
    
    html_node = markdown_to_html_node(data)
    content = html_node.to_html()
    title = extract_title(data)
    
    template_with_content = insert_text_at_template(title, template_data, "{{ Title }}")
    template_with_content = insert_text_at_template(content, template_with_content, "{{ Content }}")
    
    dest_folder = os.path.dirname(dest_path)
    
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    
    if os.path.exists(dest_path):
        os.remove(dest_path)
        
    with open(dest_path, "x") as f:
        f.write(template_with_content)

    
def insert_text_at_template(text, template_html, location):
    # could use .replace() but I wanted to remove white space if present
    updated_template = template_html.split(location)
    return f"{updated_template[0].strip()}{text}{updated_template[1].strip()}"