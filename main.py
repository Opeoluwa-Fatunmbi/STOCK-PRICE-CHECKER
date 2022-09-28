from wallstreet import Stock, Call, Put
import datetime






class StockPriceChecker:
    


    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        # self.instrument = intrument

    def full_name(self):
        # self.first_name = input("FIRST NAME: ")
        # self.last_name = input("LAST NAME: ")
        return f'{self.first_name} {self.last_name}'
    
    # @classmethod
    def get_price_of_instrument(self): 
        stock_name = input("What is the stock? ")  
        stock_price = Stock(stock_name)
        return stock_price.price







First_Trader = StockPriceChecker("John","Doe")
print(First_Trader.get_price_of_instrument())
