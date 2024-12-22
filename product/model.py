class Product:
    """
    Represents a product with various attributes such as id, name, stock, taxes, and prices.
    """

    def __init__(self, product_id, name, stock, buy_tax, sell_tax, price, last_price=None):
        """
        Initializes a new product instance.
        """
        self.id = product_id
        self.name = name
        self.stock = stock
        self.buy_tax = buy_tax
        self.sell_tax = sell_tax
        self.price = price
        self.last_price = last_price if last_price else price

        print('[INFO] Created product with values: id={self.id}; name={self.name}; stock={self.stock}; \
               buy_tax={self.buy_tax}; sell_tax={self.sell_tax}; price={self.price}; last_price={self.last_price}')

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        data = {
            'id': self.id,
            'name': self.name,
            'stock': self.stock,
            'buy_tax': self.buy_tax,
            'sell_tax': self.sell_tax,
            'price': self.price,
            'last_price': self.last_price
        }
        return str(data)


    ####
    ## Class decorators
    ####

    def __hasStock(func):
        """
        Decorator to check if the product has stock before performing an action.
        """
        def wrapper(self):
            if self.stock == 0:
                raise Exception(f'[ERROR] Item {self.id} "{self.name}" has not stock')
            return func(self)
        return wrapper
        

    ####
    ## Class public methods
    ####

    @__hasStock
    def buy(self):
        """
        Buys the product, decreasing stock and increasing price.
        """
        self.stock -= 1
        self.price *= 1 + (self.buy_tax / 1000)
        print(f'[INFO] Item {self.id} "{self.name}" bought')
        return True

    def sell(self):
        """
        Sells the product, increasing stock and decreasing price.
        """
        self.stock += 1
        self.price *= 1 - (self.sell_tax  / 1000)
        print(f'[INFO] Item {self.id} "{self.name}" sold')
        return True
    
    def save_price(self):
        """
        Saves the current price as the last price.
        """
        self.last_price = self.price
        return True
