
def valIban():
    while True:
        iban = input("Input IBAN:")
        if len(iban) == 24:
            ib = iban[0:4]
            an = iban[4:len(iban)]

            if ib[0] == "E" and ib[1] == "S" and str(an).isdecimal():
                ib = ib.replace("E", "14")
                ib = ib.replace("S", "28")
                ib = ib[0:4] + "00"

                an += ib

                ibanNum = int(an)
                ibanNum = ibanNum % 97
                ibanNum = 98 - ibanNum

                if ibanNum == 91:
                    return iban
                
        print("Incorrect IBAN")

def valFloat(type):
    while True:
        num = input("Input " + type + ":")
        try:
            num = float(num)
            return num
        except:
            print("Incorrect " + type)
