from PIL import Image
import os

class ImageConverter:
    """
    A class to handle image format conversion and compression using Pillow.
    """
    def __init__(self, input_dir: str, output_dir: str):
        """
        Initialize the ImageConverter with input and output directories.

        :param input_dir: Directory containing input images.
        :param output_dir: Directory to save converted images.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Create a set of valid extensions without leading dots
        self.valid_extensions = {ext.lstrip('.').upper() for ext in Image.registered_extensions()}

    def convert_images(self, target_format: str, compression: dict = None):
        """
        Convert and optionally compress all images in the input directory to the specified format.

        :param target_format: The target format to convert images to (e.g., 'jpeg', 'png').
        :param compression: A dictionary specifying the compression options.
                            For JPEG: {'quality': 85}
                            For PNG: {'optimize': True, 'compress_level': 9}
                            For TIFF: {'compression': 'tiff_deflate'}
                            For GIF: {'optimize': True}
        """
        images = os.listdir(self.input_dir)

        for img in images:
            try:
                # Extract the file extension and check if it is supported
                file_extension = img.split('.')[-1].upper()
                if file_extension in self.valid_extensions:
                    self._convert_image(img, target_format, compression)
                else:
                    print(f"Skipping {img}: unsupported format")
            except Exception as e:
                print(f"Failed to convert {img}: {e}")

        print('Conversion Completed')

    def _convert_image(self, img: str, target_format: str, compression: dict):
        """
        Convert and optionally compress a single image to the specified format.

        :param img: The name of the image file to convert.
        :param target_format: The target format to convert the image to.
        :param compression: A dictionary specifying the compression options.
        """
        image_path = os.path.join(self.input_dir, img)
        image = Image.open(image_path)

        # Convert to RGB if the target format is JPEG/JPG and image is in RGBA mode
        if target_format.lower() in ['jpeg', 'jpg'] and image.mode == 'RGBA':
            image = image.convert('RGB')

        converted_image = os.path.splitext(img)[0] + "." + target_format.lower()
        output_path = os.path.join(self.output_dir, converted_image)

        # Save the image with the specified compression settings
        save_kwargs = {}
        if target_format.lower() in ['jpeg', 'jpg']:
            if compression and 'quality' in compression:
                save_kwargs['quality'] = compression['quality']
        elif target_format.lower() == 'png':
            if compression:
                if 'optimize' in compression:
                    save_kwargs['optimize'] = compression['optimize']
                if 'compress_level' in compression:
                    save_kwargs['compress_level'] = compression['compress_level']
        elif target_format.lower() == 'gif':
            if compression and 'optimize' in compression:
                save_kwargs['optimize'] = compression['optimize']
        elif target_format.lower() == 'tiff':
            if compression and 'compression' in compression:
                save_kwargs['compression'] = compression['compression']

        image.save(output_path, format=target_format.upper(), **save_kwargs)
        print(f"Converted {img} to {target_format} with compression {compression}")

# Example usage
if __name__ == "__main__":
    converter = ImageConverter('static/input_images/', 'static/output_images/')
    converter.convert_images('jpeg', compression={'quality': 85})
    converter.convert_images('png', compression={'optimize': True, 'compress_level': 9})
    converter.convert_images('tiff', compression={'compression': 'tiff_deflate'})
    converter.convert_images('gif', compression={'optimize': True})
