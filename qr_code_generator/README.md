# QR Code Generator

This Python script generates a QR code for a given URL and saves it as a unique `.jpg` file. It ensures that if a file with the same name already exists, the script will create a new file with an incremented number to avoid overwriting any existing files.

## Requirements

- Python 3.x
- The `qrcode` library (can be installed using `pip install qrcode`)

## How it works

1. **User Input**: The script prompts the user to input a link or URL that they want to encode into a QR code.
2. **File Naming**: The script checks the directory for existing files named `qrcode1.jpg`, `qrcode2.jpg`, etc., and automatically assigns the next available file name to avoid overwriting.
3. **QR Code Generation**: Once the file name is determined, the script generates a QR code for the provided link using the `qrcode` library.
4. **Saving the File**: The QR code image is saved in the current directory with the generated file name.

## Code Explanation

### Functions

1. **`generate_qr_code(link, file_name)`**
   - This function generates the QR code image for the provided `link` and saves it as the specified `file_name`.
   - The QR code is created with the following parameters:
     - **Version 1**: This defines the size of the QR code. Version 1 represents a 21x21 grid.
     - **Error Correction Level L**: This allows for a 7% error correction capability in the QR code.
     - **Box Size 10**: This defines the pixel size of each "box" in the QR code.
     - **Border 4**: The thickness of the border (measured in boxes).
   - The image is saved as a `.jpg` file.

2. **`get_next_file_name(base_name, extension)`**
   - This function ensures that the script does not overwrite any existing QR code files.
   - It starts with an index of 1 and checks if a file with the name `base_name{index}{extension}` already exists. If it does, it increments the index and checks again.
   - It returns the first available file name that does not already exist.

### Main Execution

- **User Input**: The script first asks the user to input a URL or link.
- **File Name Generation**: The script generates the next available file name using `get_next_file_name()`.
- **QR Code Creation**: The script then calls `generate_qr_code()` to create and save the QR code with the generated file name.

## Usage

1. Clone or download this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install qrcode
   ```
3. Run the script:
   ```bash
   python generate_qr_code.py
   ```
4. Enter the link you want to encode as a QR code when prompted.
5. The script will generate and save the QR code in the current directory with a unique file name like `qrcode1.jpg`, `qrcode2.jpg`, etc.

## Example

Input:
```
Insert link to generate QR code: https://www.example.com
```

Output:
```
QR code generated and saved as 'qrcode1.jpg'
```
