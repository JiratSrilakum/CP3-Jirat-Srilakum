def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7/100)
    return result
price = float(input("Enter the number : "))
print(vatCalculate(price))