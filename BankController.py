from BankModel import *

class BankController():
    def __init__(self):
        self.__data = {}

    def exist(self, dni):
        if dni in self.__data:
            return True
        return False
    
    def addPortfolio(self, dni, name, surname, acountNum, balance):
        if not dni in self.__data:
            portfolio = BankModel(dni, name, surname, acountNum, balance)
            self.__data[dni] = portfolio
            return True
        return False

    def delPortfolio(self, dni):
        if dni in self.__data:
            if len(self.__data[dni].getStocks()) == 0:
                return self.__data.pop(dni)
        return None

    def getPortfolio(self, dni):
        if dni in self.__data:
            return self.__data[dni]
        return None

    def buyStock(self, dni, product, quant, price):
        portfolio = self.__data[dni]

        if (portfolio.getBalance() - (float(quant) * float(price))) >= 0:
            portfolio.setBalance(portfolio.getBalance() - (float(quant) * float(price)))
            portfolio.addStocks([product, int(quant)])
            return True
        else:
            return False      

    def sellStock(self,dni , item, quant, price):
        portfolio = self.__data[dni]
        stock = portfolio.getStocks()[item]

        if stock[1] - quant >= 0:
            portfolio.setBalance((price * quant) + portfolio.getBalance())
            stock[1] = stock[1] - quant
            portfolio.sellStocks(stock)
            return True
        return False


    def getPortCount(self):
        return len(self.__data)
    