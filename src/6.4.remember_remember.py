"""
This module extracts hidden messages from an image by analyzing the color of its pixels.
Functions:
- remember_remember(image_path): Scans an image for black pixels (defined as pixels with all RGB 
  values below or equal to 50) and constructs a message by interpreting the position of these black pixels.
  The message is built by using the pixel's y-coordinate (ranging from ASCII values 32 to 126) to extract 
  characters from the image.
"""

from PIL import Image

DEFAULT_IMAGE_PATH = "resources/code.png"

def remember_remember(image_path):
    """The function tries to extract a hidden message from an image by looking for black pixels."""
    try:
        img = Image.open(image_path).convert("RGB")
    except (OSError, IOError) as e:
        print(f"Error loading image: {e}")
        return ""

    width, height = img.size
    pixels = img.load()
    message = []

    def is_black(pixel):
        """Checks if a pixel is mostly black."""
        return all(channel <= 50 for channel in pixel)

    for x in range(width):
        for y in range(height):
            if is_black(pixels[x, y]):
                # Use the y-coordinate as an ASCII code, ensuring it's within the readable character range
                if 32 <= y <= 126:
                    message.append(chr(y))

    return "".join(message)

if __name__ == "__main__":
    print("Hidden message:", remember_remember(DEFAULT_IMAGE_PATH))
