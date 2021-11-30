import requests

def getStocksApi():
    url = "https://bb-finance.p.rapidapi.com/market/get-full"
    querystring = {"id":"ANA:SM,ACX:SM,ACS:SM,SAN:SM,BBVA:SM,CABK:SM,CLNX:SM,ENG:SM,ELE:SM,FER:SM,GRF:SM,IAG:SM,IBE:SM,ITX:SM,IDR:SM,MAP:SM,MEL:SM,NTGY:SM,REP:SM,TEF:SM"}
    headers = {
        'x-rapidapi-host': "bb-finance.p.rapidapi.com",
        'x-rapidapi-key': "a365ad1a8cmsh8c4907a923c8b44p1ddecajsn2ec4d759c257"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

"""
data = json.loads(response.text)

stocks = {}
print("List of stocks")
print("--------------")
for stock, values in data["result"].items():
    print("Stock key:", stock, " -> ", values["name"], "Price: ", values["last"])
    stocks[stock] = (values["name"], values["last"])  

stock = input("Select stock:")
print(stock, stocks[stock][0], stocks[stock][1])
"""