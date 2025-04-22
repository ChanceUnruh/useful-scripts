# PDF to PNG Converter

This Python script converts each page of a PDF document into a separate PNG image. The images are saved in the same directory as the PDF file, and each page is assigned a unique filename to prevent overwriting.

## Requirements

- Python 3.x
- The `PyMuPDF` library (install using `pip install pymupdf`)
- The `Pillow` library (install using `pip install pillow`)

## How it works

1. **User Input**: The script requires the path to a PDF file, which should be provided in the `pdf_path` variable.
2. **File Processing**: The script opens the PDF using the PyMuPDF library, then iterates over each page to convert it to a pixmap (image data).
3. **Image Conversion**: Each page is converted to a PNG image using the Pillow library, and the images are saved in the same folder as the PDF.
4. **Unique Filenames**: The script ensures that each page of the PDF is saved as a separate image, with filenames like `Your_file_name1.png`, `Your_file_name2.png`, etc., so no files are overwritten.

## Code Explanation

### Steps:
1. **PDF Path Setup**:
   The path to the PDF file is set in the `pdf_path` variable.
   
2. **Opening the PDF**:
   The script opens the PDF file using `fitz.open(pdf_path)`.

3. **Page Conversion**:
   For each page in the PDF:
   - The page is rendered as a pixmap (image data) using `page.get_pixmap()`.
   - The pixmap is then converted to a Pillow Image object for further manipulation.
   
4. **Saving the Image**:
   The image is saved as a PNG file in the same folder as the PDF. The filename includes the page number (e.g., `Your_file_name1.png`, `Your_file_name2.png`), ensuring that no files are overwritten.

5. **Completion**:
   After all pages have been processed, a message is printed to indicate that the conversion is complete.

## Example Output

- If the input PDF has 3 pages, the script will generate the following PNG files:
  - `Your_file_name1.png`
  - `Your_file_name2.png`
  - `Your_file_name3.png`
