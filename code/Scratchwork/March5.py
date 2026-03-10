stocks = 'AAPL,MSFT,GOOG,AMZN'

stock_list = stocks.split(',')
print(stock_list)

stock_string = ",".join(stock_list)
print(stock_string)


print("OGP" in stock_string)
# print(stocks[0])
# print(stocks[-1])

# print(stocks + ",TSLA")


# print(stocks.lower())

# print(stocks.find("MSFT"))

# print(sorted(stocks, reverse = True))

# print(stocks.strip("A"))

# def count_vowels(s):
#     count = 0
#     for c in s:
#         if c in 'aeiou':
#             count += 1
#             return count
#     return count

# print(count_vowels('apple'))
# print(count_vowels('sky'))


# def count_vowels(s):
#     count = 0
#     for c in s:
#         if c in 'aeiou':
#             count += 1
            
#     return count

# print(count_vowels('apple'))
# print(count_vowels('sky'))