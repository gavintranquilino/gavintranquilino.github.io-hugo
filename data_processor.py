#!/usr/bin/env python3
"""
Data processing utility for image files.
"""

import sys
from PIL import Image
from pathlib import Path


def remove_exif(image_path):
    """
    Remove EXIF data from an image file.
    
    Args:
        image_path (Path): Path to the image file
    """
    try:
        with Image.open(image_path) as img:
            # Create a new image without EXIF data
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(list(img.getdata()))
            
            # Save back to the same location
            if img.format == 'JPEG':
                clean_img.save(image_path, 'JPEG', quality=95, optimize=True)
            else:
                clean_img.save(image_path, img.format)
            
            print(f"Cleaned: {image_path.name}")
            return True
            
    except Exception as e:
        print(f"Error processing {image_path.name}: {str(e)}")
        return False


def main():
    """Remove EXIF data from all images in specified directory or default to static/img."""
    # Check if a path argument was provided
    if len(sys.argv) > 1:
        img_dir = Path(sys.argv[1])
    else:
        img_dir = Path("static/img")
    
    if not img_dir.exists():
        print(f"Directory not found: {img_dir}")
        return
    
    supported_formats = {'.jpg', '.jpeg', '.png', '.tiff', '.tif', '.bmp'}
    processed_count = 0
    print(f"Processing images in {img_dir} (recursively)...")
    
    for file_path in img_dir.glob("**/*"):
        if file_path.is_file() and file_path.suffix.lower() in supported_formats:
            if remove_exif(file_path):
                processed_count += 1
    
    print(f"\nDone! Processed {processed_count} images.")


if __name__ == "__main__":
    main()
