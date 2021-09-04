with open('currency.txt') as f:
	lines = f.readlines()
currencyDict = {}
for line in lines:
	currsplit = line.split("\t")
	currencyDict[currsplit[0]] = currsplit[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert :\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
