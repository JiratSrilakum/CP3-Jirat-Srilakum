def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "000":
        return showMenu()
    else:
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Choose type : "))
    if userSelected==1:
        price = int(input("Price : "))
        print("After calculate vat =",vatCalculate(price),"THB")
    elif userSelected==2:
        print("Total price =",priceCalculate(),"THB")
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()
