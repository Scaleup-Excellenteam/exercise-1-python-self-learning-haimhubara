def piece_of_cake(dictionary, optional=None):
    """
    The func calculate the price of the products

    params: dictionary and  optional list
    return: price off all the keys in the dictionary that not in optional list
    """
    if optional is None:
        optional = []
    price_of_recipe = 0
    for key, value in dictionary.items():
        if value not in optional:
            price_of_recipe += key

    return price_of_recipe



if __name__ == "__main__":
    price = piece_of_cake({100:'tomato',300:'banana'},['tomato'])
    print("price: " , price )
