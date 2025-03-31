from PIL import Image

def remember_remember(image_path):
    """
    The function try to extract hidden message from image by looking on black pixels

    params: path to image
    return: hidden message
    """
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error loading image: {e}")
        exit()

    width, height = img.size
    pixels = img.load()
    message = ""

    def is_black(pixel):

        return all(channel <= 50 for channel in pixel)

    for x in range(width):
        for y in range(height):
            if is_black(pixels[x, y]):
                print(f"Found black pixel at ({x}, {y})")

                if 32 <= y <= 126:
                    message += chr(y)

    return message


if __name__ == "__main__":
    image_path = "resources/code.png"
    hidden_message = remember_remember(image_path)
    print("Hidden message:", hidden_message)
