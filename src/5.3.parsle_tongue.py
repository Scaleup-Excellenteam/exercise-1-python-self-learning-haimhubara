"""
This module extracts hidden messages from a binary file.
Functions:
- parsle_tongue(file_path): Scans a binary file and extracts hidden words that match a specific pattern. 
  The function looks for words with at least five lowercase letters followed by an exclamation mark (!).
"""

import re

def parsle_tongue(file_path):
    """
    The function tries to extract a hidden sentence from a binary file.

    params:
    - file_path (str): Path to the binary file.

    return:
    - A set of extracted hidden messages (strings).
    """

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
    file_path = 'logo.jpg'
    secret_messages = parsle_tongue(file_path)
    for message in secret_messages:
        print(message)
