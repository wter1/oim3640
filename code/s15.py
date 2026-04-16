#Using library according to your needs 
#When doing loop refer to k for keys



names = {"renee": 96, "aurora": 94, "amelia": 95}

for i, value in enumerate(names.values()):
    print(i, value)

order = sorted(names.values())

current_max = float("-inf")

current_max = 0 

for grade in names.values():
    if grade > current_max:
        current_max = grade

print(current_max)


# names_list = []
# for name in names:
#     grade = float(names.values())
#     if grade > 94:
#         names_list.append(name)

# print(names_list)

def get_expensive_stocks(stocks, p):
    expensive_stocks = []
    for name, price in prices.items():
        if price >= 200:
            expensive_stocks.append(name)
    return expensive_stocks



# for i in prices.values():
#     price *= 1.1

for name in names:
    grade = names[name]
    names[name] = grade + 2

print(names)


