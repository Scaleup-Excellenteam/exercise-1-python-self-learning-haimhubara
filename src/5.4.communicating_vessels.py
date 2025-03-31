from itertools import zip_longest

def communicating_vessels(*iterables):
    """
    The func take cpuple iterators and uninte them one by one

    params: iterators
    return: list of all the item from all the iterators one by one
    
    """
    for items in zip_longest(*iterables, fillvalue=object()):
        for item in items:
            if item is not object():
                yield item

if __name__ == "__main__":
    result = list(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    print(result) 
