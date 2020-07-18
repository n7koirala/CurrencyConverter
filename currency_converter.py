import json
from urllib.request import urlopen

with urlopen("https://api.exchangeratesapi.io/latest?base=USD") as response:
    source = response.read()

data = json.loads(source)


# function for coversion
def convertCurrency(amount, _from, _to):

    rateArray = data["rates"]

    fromR = rateArray.get(_from)
    toR = rateArray.get(_to)

    total = amount * toR / fromR
    print(str(amount) + " " + _from + " = " + str(total) + " " + _to)


# making visually helpful
countryList = list(data["rates"])
print("Currently available countries: ")
for country in countryList:
    print(country)
print("Last Update: " + data["date"])

convertCurrency(10, "USD", "GBP")
