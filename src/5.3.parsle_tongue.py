"""
This module extracts hidden messages from a binary file.
Functions:
- parsle_tongue(file_path): Scans a binary file and extracts hidden words that match a specific pattern. 
  The function looks for words with at least five lowercase letters followed by an exclamation mark (!).
"""

import re
import os

def parsle_tongue(file_path=None):
    """
    The function tries to extract a hidden sentence from a binary file.

    params:
    - file_path (str): Path to the binary file. If None, it defaults to a predefined file.

    return:
    - A set of extracted hidden messages (strings).
    """
    # If no file_path is provided, set a default one
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), 'logo.jpg')  # Default file path

    pattern = re.compile(rb'[a-z]{5,}!')
    chunk_size = 4096

    messages = set()

    with open(file_path, 'rb') as file:
        data = b''
        while chunk := file.read(chunk_size):
            data += chunk
            matches = pattern.findall(data)
            for match in matches:
                messages.add(match.decode())

            data = data[-(len(pattern.pattern) * 2):]

    return messages

if __name__ == "__main__":
    # If the script is run directly, it will use the default file path
    secret_messages = parsle_tongue()
    for message in secret_messages:
        print(message)
