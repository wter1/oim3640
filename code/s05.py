# A product would cost $100, how much tax do we pay?

# product = 100 # in dollars
# tax_rate = 0.0625
# tax = product * tax_rate
# print(f"The tax for product which costs ${product} is ${tax}") # f stands for formatted string

computer_price = 900
iphone_price = 1100
mass_rate = 0.0625

def calc_tax(product_price, tax_rate):
    """Calculate product tax based on given price"""
    # tax_rate = 0.0625
    tax = product_price * tax_rate
    # print(f"The tax for product which costs ${product_price} is ${tax}") # f stands for formatted string
    # print(tax)
    # if function doesn't explicitly return any value it would return None
    return tax
    
calc_tax(computer_price, mass_rate)
calc_tax(iphone_price, mass_rate)

total_tax = calc_tax(computer_price, mass_rate) + calc_tax(iphone_price, mass_rate)
print(total_tax)








