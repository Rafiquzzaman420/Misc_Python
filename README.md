# Image Converter

A Python class to handle image format conversion and compression using the Pillow library.

## Features

- Convert images to various formats (JPEG, PNG, GIF, TIFF).
- Optional compression for supported formats.
- Supports various compression methods provided by Pillow.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Rafiquzzaman420/Misc_Python
    cd Misc_Python
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` includes:
    ```plaintext
    Pillow
    ```

## Usage

1. Import the `ImageConverter` class.
2. Create an instance of `ImageConverter` with input and output directories.
3. Call the `convert_images` method with the target format and optional compression settings.

### Example

```python
from ImageConverter import ImageConverter

# Initialize the converter with input and output directories
converter = ImageConverter('static/input_images/', 'static/output_images/')

# Convert images to JPEG with quality compression
converter.convert_images('jpeg', compression={'quality': 85})

# Convert images to PNG with optimization and compression level
converter.convert_images('png', compression={'optimize': True, 'compress_level': 9})

# Convert images to TIFF with deflate compression
converter.convert_images('tiff', compression={'compression': 'tiff_deflate'})

# Convert images to GIF with optimization
converter.convert_images('gif', compression={'optimize': True})
