"""
This module provides file-related functions.
Functions:
- thats_the_way(path): Receives a directory path and returns a list of filenames that start with "deep". 
  If the directory does not exist, it prints an error message and returns an empty list.
"""


import os

def thats_the_way(path):
    """ 
    get path to file name and tell us the names of the files that start with deep

    params: path to file name
    return: files that start with deep
    """
    try:

        # give list of all the files inside the path
        all_entries = os.listdir(path)

        # we want just the files that start with deep
        deep_files = [
            file_name for file_name in all_entries
            if file_name.startswith("deep") and os.path.isfile(os.path.join(path, file_name))
        ]

        return deep_files

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return []



if __name__ == "__main__":
    result = thats_the_way("images")
    print(result)
