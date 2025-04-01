"""
This module extracts hidden messages from an image by analyzing the color of its pixels.
Functions:
- remember_remember(image_path): Scans an image for black pixels (defined as pixels with all RGB 
  values below or equal to 50) and constructs a message by interpreting the position of these black pixels.
  The message is built by using the pixel's y-coordinate (ranging from ASCII values 32 to 126) to extract 
  characters from the image.
"""

from PIL import Image

def remember_remember(image_path):
    """
    The function tries to extract a hidden message from an image by looking for black pixels.

    This function loads an image from the given path, scans it pixel



from PIL import Image

def remember_remember(image_path):
    """
    The function tries to extract a hidden message from an image by looking for black pixels.

    params:
    - image_path (str): The path to the image.

    return:
    - (str): The hidden message extracted from the image.
    """
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""

    width, height = img.size
    pixels = img.load()
    message = []

    def is_black(pixel):
        """ 
        Checks if a pixel is mostly black

        params: 
        - pixel

        return:
        - true if is black else false

        """
        return all(channel <= 50 for channel in pixel)

    for x in range(width):
        for y in range(height):
            if is_black(pixels[x, y]):
                # Here, we expect the black pixel locations to correspond to certain character data
                # For the purpose of this example, we will need a proper algorithm for decoding
                # For now, it's just a placeholder message.
                message.append("X")

    return "".join(message)


if __name__ == "__main__":
    image_path = "resources/code.png"
    hidden_message = remember_remember(image_path)
    print("Hidden message:", hidden_message)
