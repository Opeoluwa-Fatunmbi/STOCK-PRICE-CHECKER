from wallstreet import Stock, Call, Put
import datetime


class StockPriceChecker:

    
    def __init__(self, first_name, last_name, intrument) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.instrument = intrument

    def full_name(self):
        self.first_name = input("FIRST NAME: ")
        self.last_name = input("LAST NAME: ")
        return f'{self.first_name} {self.last_name}'
    

    def get_price_of_instrument(self):
        s = Stock('AAPL')
        print(s.price)






First_Trader = StockPriceChecker("John","Doe","")
