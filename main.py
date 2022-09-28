from unicodedata import name
from wallstreet import Stock, Call, Put
import datetime






class StockPriceChecker:
    


    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name


    def investor_name(self):
        self.first_name = input("FIRST NAME: ")
        self.last_name = input("LAST NAME: ")
        return f'{self.first_name} {self.last_name}'

    
    # @classmethod
    def get_price_of_instrument(self): 
        stock_name = input("What is the stock? ")  
        stock_price = Stock(stock_name)
        return f'Hiii {self.first_name} {self.last_name}, the price of {stock_name} is {stock_price.price} at {datetime.datetime.now()}'







First_Trader = StockPriceChecker("John","Doe")

if __name__ == "__main__":
    First_Trader.investor_name()
    print(First_Trader.get_price_of_instrument())
