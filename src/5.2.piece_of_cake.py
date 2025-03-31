def piece_of_cake(dictionary, optional=None):
    """
    The func calculates the total price of products.

    :param dictionary: A dictionary where keys are prices and values are product names.
    :param optional: A list of product names to exclude (default is None).
    :return: The total price of all products not in the optional list.
    """
    if optional is None:
        optional = []
    
    price_of_recipe = 0
    for price, product in dictionary.items():
        if product not in optional: 
            price_of_recipe += price  

    return price_of_recipe


if __name__ == "__main__":
    price = piece_of_cake({100: 'tomato', 300: 'banana'}, ['tomato',])
    print("price:", price) 