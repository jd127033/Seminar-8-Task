class Product:
    """Represent a Product object."""

    def __init__(self, name="", price=0):
        """Initialise a Product instance.
        Price: Price of product
        """
        self.name = name
        self.price = price

    def __str__(self):
        """ String representation of Product object"""
        return f"{self.name}: ${self.price}"


