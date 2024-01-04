import sys
import fitz

def invert_colors(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page_num in range(doc.page_count):
        page = doc[page_num]

        # Invert the colors for the entire page
        page.invert_irect(page.rect)

    doc.save(output_pdf)
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python invert_colors.py input.pdf output_inverted.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]

    invert_colors(input_pdf, output_pdf)
    print(f"Colors inverted. Output saved to {output_pdf}")
