from __future__ import annotations
import logging
from types import NotImplementedType

class Product:
    '''
        Code for the Product class goes here
        Product has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
    '''
    #Static loger variable to log all issues to do with the Product class  
    logger = logging.getLogger(__name__)


    __ID_PREFIX = "PROD_"
    def __init__(self, id: str, name: str, cost_price: float, retail_price: float, quantity: int):
        """
        Initializes a Product object with the given parameters.
        Args:
            id (int): The unique identifier for the product.
            name (str): The name of the product.
            cost_price (float): The cost price of the product.
            retail_price (float): The retail price of the product.
            quantity (int): The quantity of the product in stock.
        """
        # Check if the year is valid 
        if Product.validate_id(id):
            # 
            id = id.upper()
            self._id = id
        else:
            raise ValueError("ID value invalid")
        
        self.name = name

    # Creating Validations
        def validate_id(id: int) -> bool:
            """
            Validates the id of the product.
            Args:
                id (int): The unique identifier for the product.
            Returns:
                bool: True if the id is valid, False otherwise.
            """
            if id is None:
                print("ID cannot be None.")
                return False
            
            if not id.upper().startswith(Product.__ID_PREFIX):
                print("ID must start with 'P'.")
                return False
            
            return True
        
        def validate_cost_price(cost_price: float) -> bool:
            """            
            Validates the cost price of the product
            Args:
                cost_price (float): The cost price of the product.
            """
            # 
            if cost_price is None:
                print("Price cannot be None")
                return False
            
            #
            if cost_price <= 0:
                print("Invalid cost price - price must be greater than 0")
                return False
            
            return True
            
        
