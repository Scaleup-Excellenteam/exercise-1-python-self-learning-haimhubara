"""
This module provides a function to group elements of an iterable based on a specific function applied to each element. 
The `group_by` function allows grouping by various criteria, such as length of strings, modulo values, or custom logic defined by the user.
Functions:
- group_by(func, iterable): Groups elements of the iterable based on the result of applying the given function to each element. 
  It returns a dictionary where the keys are the results of the function and the values are lists of items that share the same result.
"""

def group_by(func, iterable):
    """
    The function takes a list of strings (or any iterable) and divides them into groups based on the result of 
    applying a function to each element (such as string length, modulo operation, or other custom logic).

    params:
    - func (function): A function that will be applied to each item in the iterable to determine its group.
    - iterable (iterable): A list (or any iterable) to be grouped.

    return:
    - dict: A dictionary where keys are the results of applying the function (`func`) to each item in the iterable, 
      and the values are lists of items that produce the same result.
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


if __name__ == "__main__":
    result = group_by(len, ["hi", "bye", "yo", "try", "mont"])
    print(result)
