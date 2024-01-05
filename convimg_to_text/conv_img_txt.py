import os
import sys
import pytesseract
from PIL import Image

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python image_to_text.py <path_to_image>")
        sys.exit(1)

    image_file = sys.argv[1]

    print(ocr_core(image_file))

    print(f"Successfully converted {image_file}")
