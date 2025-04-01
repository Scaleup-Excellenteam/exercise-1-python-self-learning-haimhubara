"""
This module provides a function for calculating the total price of selected products.
Functions:
- piece_of_cake(prices, optionals=None, **kwargs):  
  Calculates the total price of products based on given prices per 100 units and the quantities provided.
"""

def piece_of_cake(prices, optionals=None, **kwargs):
    """
    Calculates the total price of selected products.

    :param prices: A dictionary where keys are product names and values are their prices per 100 units.
    :param optionals: A list of product names to exclude (default is None).
    :param kwargs: Quantities of products in units.
    :return: The total price of all products not in the optional list.
    """
    if optionals is None:
        optionals = []

    total_price = 0.0
    for product, price_per_100 in prices.items():
        if product not in optionals and product in kwargs:
            total_price += (price_per_100 / 100) * kwargs[product]

    return total_price


if __name__ == "__main__":
    price = piece_of_cake({'tomato': 100, 'banana': 300}, ['tomato'], banana=200)
    print("price:", price)