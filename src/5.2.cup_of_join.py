"""
This module provides list manipulation functions.
Functions:
- cup_of_join(*args, sep=None): Merges multiple lists into one. If a separator is provided, 
  it is inserted between every two lists.
"""

def cup_of_join(*args, sep=None):
    """
    The function receives multiple lists and merges them into one list.
    If a separator is provided, it is inserted between every two lists.

    params:
    - *args: Any number of lists.
    - sep (optional): The separator to insert between lists.

    return:
    - A merged list with the separator (if provided) between lists.
    """
    result_list = []
    for i, lst in enumerate(args):
        if i > 0 and sep is not None:  # Add separator only between lists (not at the end)
            result_list.append(sep)
        result_list.extend(lst)  # Add list elements

    return result_list


if __name__ == "__main__":
    result_list = cup_of_join([12, 12, 12], [12, 12, 12])
    print("result_list:", result_list)
