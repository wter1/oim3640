# # #TODO: Review Question 1
# # words = 'the cat sat on the mat'.split()
# # print(len(words))
# # print(len(set(words)))


# # #TODO: Review Question 2
# # def mystery(s):
# #     return len(set(s)) == len(s)

# # print(mystery('hello')) #False
# # print(mystery('world')) #True


# # #TODO: Review Question 3
# # import yfinance as yf
# # from pprint import pprint

# # tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
# # stocks = {}

# # for t in tickers:
# #     stocks[t] = yf.Ticker(t).info["currentPrice"]


# # pprint(stocks) #Neat printing (Automatically sorts)
# # print(stocks.keys())

# # print("After sorting ...")
# # print(sorted(stocks))

# # """    
# # How then, do we sort by the values and not the keys? (sorted only works on keys)
# # """

# # def sort_by_price(t):
# #     return t[1] #Checks the second value in a tuple pair 

# # print(sorted(stocks.items(), key=sort_by_price)) #.items() returns a tuple

# # print(sorted(stocks.items(), key=lambda t: t[1])) #Same thing without the requirement of a function


# #TODO: Review Question 4
# num = 100
# try: #Will catch an error, handle it and keep moving on in the code
#     a = float(input("Enter a number to divide by: "))
#     print(num / a)
# except ZeroDivisionError:
#     print("Error: Division by zero is NOT allowed.")
# except ValueError:
#     print("Error: Please enter a valid number.")
# finally:
#     print("We still want to print this!")

# print("Let's move on to the next part of the code ...")
# #Why use this instead of some for loop that can have a user reenter their values if they did it wrong the first time?
# #Whever something is out of your control (Think mistake proofing)

# names = ['Alice', 'Bob', 123, 'Charlie']
# uppercase_names = []

# for name in names:
#     try:
#         print(name.upper())
#         uppercase_names.append(name.upper())
#     except AttributeError:
#         print(f"Error: '{name}' is not a string and cannot be converted to uppercase.")

# #building on this, another use case is if you're importing a data file. More often then not there will be some error in their outputs because you're not the one that created the file









