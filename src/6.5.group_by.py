def group_by(func, iterable):
    """
    The function get list with strings and divide the to groups by the length

    params: list of strings
    return: dictionary key ins length and values is strings with length  equal to key
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


if __name__ == "__main__":
    result = group_by(len, ["hi", "bye", "yo", "try","mont"])
    print(result)


