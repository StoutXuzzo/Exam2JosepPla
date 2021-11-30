import requests, json
from BankController import *

ctrl = BankController()

def getStocksApi():
    url = "https://bb-finance.p.rapidapi.com/market/get-full"
    querystring = {"id":"ANA:SM,ACX:SM,ACS:SM,SAN:SM,BBVA:SM,CABK:SM,CLNX:SM,ENG:SM,ELE:SM,FER:SM,GRF:SM,IAG:SM,IBE:SM,ITX:SM,IDR:SM,MAP:SM,MEL:SM,NTGY:SM,REP:SM,TEF:SM"}
    headers = {
        'x-rapidapi-host': "bb-finance.p.rapidapi.com",
        'x-rapidapi-key': "a365ad1a8cmsh8c4907a923c8b44p1ddecajsn2ec4d759c257"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

while True:
    print("\nCurrently there are " + str(ctrl.getPortCount()) + " portfolios registered!")
    print("1.- Add a portfolio")
    print("2.- Delete portfolio")
    print("3.- Buy stock for a client")
    print("4.- Sell stock for a client (LIST THE CLIENT PRODUCTS, BUT SELL IS NOT IMPLEMENTED)")
    print("5.- List client portfolio ")
    print("6.- Exit")
    user = input("Choose option: ")

    if user == "1":
        dni = input("\nInput DNI: ")
        name = input("Input Name: ")
        surname = input("Input Surname: ")
        acountNum = input("Input Account Number: ")
        balance = input("Input initial balance: ")

        if ctrl.addPortfolio(dni, name, surname, acountNum, balance):
            print("Portfolio added successfully!!!")
        else:
            print("The portfolio alreadi exists.")
            
    if user == "2":
        dni = input("\nInput DNI: ")

        portfolio = ctrl.delPortfolio(dni)

        if portfolio != None:
            print("Portfolio succesfully deleted")
        else:
            print("The portfolio have stock or doesn't exist")

    if user == "3":
        
        dni = input("\nInput DNI: ")
        if ctrl.exist(dni):
            data = getStocksApi()
            stocks = {}
            print("List of stocks:")

            for stock, values in data["result"].items():
                print("\tStock key:", stock, " -> ", values["name"], "Price: ", values["last"])
                stocks[stock] = (values["name"], values["last"])  

            stock = input("Select stock: ")
            print(stock, stocks[stock][0], stocks[stock][1])
            price = stocks[stock][1]
            quant = input("Input quantity: ")

            if ctrl.buyStock(dni, stock, quant, price):
                print("Stock bought successfully")
            else:
                print("The client don't have enought money")
        else:
            print("The portfolio doesn't exist")



    if user == "4":
        
        dni = input("\nInput DNI: ")

        portfolio = ctrl.getPortfolio(dni)

        if portfolio != None:
            clientStock = portfolio.getStocks()
            data = getStocksApi()
            stocks = {}
            print("List of stocks:")

            for stock, values in data["result"].items():
                if stock in clientStock:
                    print("\tStock key:", stock, " -> ", values["name"], "Price: ", values["last"],"Client stock:", clientStock[stock][1])
                    stocks[stock] = (values["name"], values["last"])  

            stock = input("Select stock: ")
            print(stock, stocks[stock][0], stocks[stock][1])
            price = stocks[stock][1]
            quant = input("Input quantity: ")

            if ctrl.sellStock(dni, stock, int(quant), float(price)):
                print("Product selled succesfully")
            else:
                print("There is not enought stock")

        else:
            print("The portfolio doesn't exist")

    if user == "5":
        
        dni = input("\nInput DNI: ")

        portfolio = ctrl.getPortfolio(dni)

        if portfolio != None:

            print("DNI: " + portfolio.getDNI())
            print("Name: " + portfolio.getName())
            print("Surname: " + portfolio.getSurname())
            print("Account: " + str(portfolio.getAcountNum()))
            print("Balance: " + str(portfolio.getBalance()))
            print("Valores:")

            valores = portfolio.getStocks()

            for key in valores.keys():
                print("\t" + valores[key][0] + " - " + str(valores[key][1]) + " uds")
        
        else:
            print("The portfolio dosn't exist")

    if user == "6":
        break
