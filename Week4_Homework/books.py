from __future__ import annotations
from types import NotImplementedType

from products import Product

class Book(Product):
    '''
        Code for the Book class goes here
        Book has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
        an author
        one or more genres (these should be stored in a list)
    '''
    def __init__(self, id: int, name: str, cost_price: float, retail_price: float, quantity: int, author: str, genres: list[str]):
        """
        Initializes a Book object with the given parameters.
        Args:
            id (int): The unique identifier for the book.
            name (str): The name of the book.
            cost_price (float): The cost price of the book.
            retail_price (float): The retail price of the book.
            quantity (int): The quantity of the book in stock.
            author (str): The author of the book.
            genres (list[str]): A list of genres associated with the book.
        """

        