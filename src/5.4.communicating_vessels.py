from itertools import zip_longest

def interleave(*iterables):
    """
    The func takes a couple of iterators and unites them one by one.

    params: iterators
    return: list of all the items from all the iterators one by one
    """
    fill_value = object()  # יצירת אובייקט יחיד לפני הלולאה
    for items in zip_longest(*iterables, fillvalue=fill_value):
        for item in items:
            if item is not fill_value:  # השוואה לאובייקט הקבוע
                yield item

def generator_interleave(*iterables):
    """
    The func takes a couple of iterators and unites them one by one, using the generator approach.

    params: iterators
    return: list of all the items from all the iterators one by one
    """
    fill_value = object()  # יצירת אובייקט יחיד לפני הלולאה
    for items in zip_longest(*iterables, fillvalue=fill_value):
        for item in items:
            if item is not fill_value:  # השוואה לאובייקט הקבוע
                yield item

if __name__ == "__main__":
    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)
