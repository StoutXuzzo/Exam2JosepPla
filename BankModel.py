from BaseModel import *

class BankModel(BaseModel):
    def __init__(self, dni, name, surname, acountNum, balance):
        super().__init__(dni, name, surname)
        self.__acountNum = acountNum
        self.__balance = float(balance)
        self.__stocks = {}

    def getAcountNum(self):
        return self.__acountNum

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def addStocks(self, item):
        if item[0] in self.__stocks:
            self.__stocks[item[0]][1] += item[1]
        else:
            self.__stocks[item[0]] = item

    def sellStocks(self, item):
        if item[1] == 0:
            self.__stocks.pop(item[0])
        else:
            self.__stocks[item[0]] = item

    def getStocks(self):
        return self.__stocks

    