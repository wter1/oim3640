import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
print(type(info))


print(info["shortName"])
print(info["currentPrice"])


# print(info.keys())
print(len(info))
print(info["longName"])

# print(info["longBusinessSummary"].split())
print("iPhone" in info["longBusinessSummary"]) #True (Checking for the first instance of the sequence "IPhone")
print("iPhone" in info["longBusinessSummary"].split()) #False (Checking for an item named "iPhone", the problem is thatthe data is split without any specifications so you'll have iPhone still split with it's comma)


print(info["city"])
# info["city"][0] = "c"
info["city"] = "Wellesley"
print(info["city"])

info["founder"] = "Robert"
print(info["founder"])

for k, v in info.items():
    print(k, v)

#Exercises will be based on the dictionary below
tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

print(sorted(prices)) #Creates a new list of all the keys sorted alphabetically 
print(sorted(prices.values(), reverse = True))
print(list(reversed(prices.values()))) #Difference? I think it's because this one might sort by what the numbers are actually called

#How to sort stocks by values 
print(sum(prices.values()))

#or

total = 0
for price in prices.values():
    total += price
print(total)


tickers.append("GOOG")
for t in tickers:
    prices[t] = yf.Ticker(t).info["currentPrice"]

print(info.keys())

stocks = {} # {"NVDA": [open, currentPrice, volume]}
for t in tickers:
    # stocks[t] = yf.Ticker(t).info["open"], yf.Ticker(t).info["currentPrice"], yf.Ticker(t).info["volume"] #Makes the values a tuple (immutable)
    # stocks[t] = [yf.Ticker(t).info["open"], yf.Ticker(t).info["currentPrice"], yf.Ticker(t).info["volume"]] #Makes the values into a list
    info_list = {}
    for name in ["open", "currentPrice", "volume"]:
        info_list[name] = yf.Ticker(t).info[name]
    stocks[t] = info_list



telephone_number = "123-456-7890"

a, b, c = telephone_number.split("-")
print(c)

*_, ext = telephone_number.split("-")  # *_ Signifies all we care about is the last split or in context, the last 4 digits.

ext

import timeit
words = open('data/words.txt').read().split()
word_set = set(words)     # 113K+ words

def search_list():
    return 'python' in words
def search_set():
    return 'python' in word_set

print('List:', timeit.timeit(search_list, number=1000))
print('Set: ', timeit.timeit(search_set, number=1000))
# List: 0.8500s  Set: 0.0003s

print(word_set)


    