from PIL import Image
import pytesseract
import sys

def image_to_latex(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Print the LaTeX representation of the text
        print(text)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_to_latex.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    image_to_latex(image_path)
