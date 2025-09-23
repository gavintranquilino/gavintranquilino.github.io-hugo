#!/usr/bin/env python3

import os
import re
import sys

def process_markdown_file(file_path):
    """Process a markdown file to convert image references and add img shortcode"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to match markdown image syntax: ![alt text](/img/path/to/image.ext)
    img_pattern = r'!\[([^\]]*)\]\((/img/[^)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        old_path = match.group(2)  # e.g., "/img/wato-humanoid/cover.png"
        
        # Remove the "/img/" prefix to get the relative path
        # e.g., "/img/wato-humanoid/cover.png" -> "wato-humanoid/cover.png"
        new_path = old_path.replace('/img/', '')
        
        # Create the shortcode with proper parameters
        if alt_text:
            shortcode = f'{{{{< img src="{new_path}" alt="{alt_text}" >}}}}'
        else:
            shortcode = f'{{{{< img src="{new_path}" >}}}}'
        
        return shortcode
    
    # Replace all image references
    content = re.sub(img_pattern, replace_image, content)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    projects_dir = '/mnt/storage/Projects/hugo/content/projects'
    
    if not os.path.exists(projects_dir):
        print(f"Error: Projects directory not found: {projects_dir}")
        return 1
    
    files_processed = 0
    files_changed = 0
    
    for filename in os.listdir(projects_dir):
        if filename.endswith('.md') and filename != '.gitkeep':
            file_path = os.path.join(projects_dir, filename)
            print(f"Processing: {filename}")
            
            try:
                changed = process_markdown_file(file_path)
                files_processed += 1
                if changed:
                    files_changed += 1
                    print(f"  ✓ Updated image references")
                else:
                    print(f"  - No changes needed")
            except Exception as e:
                print(f"  ✗ Error processing file: {e}")
    
    print(f"\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
