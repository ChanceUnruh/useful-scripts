import fitz  # PyMuPDF
from PIL import Image
import os

# Path to your PDF file
pdf_path = r"Your\\file\\path\\here.pdf"

# Output folder (same as PDF location)
output_folder = os.path.dirname(pdf_path)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Convert each page to an image
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    
    # Render page as a pixmap (image data)
    pix = page.get_pixmap()

    # Convert to PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save as PNG
    output_file = os.path.join(output_folder, f"Your_file_name{page_num+1}.png")
    img.save(output_file, "PNG")

print("Conversion complete! Images saved in:", output_folder)
