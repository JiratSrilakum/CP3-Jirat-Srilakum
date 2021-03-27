menuList = []
priceList = []
def showBill():
    totalPrice = 0
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i],"->",priceList[i],"THB")
        totalPrice = int(priceList[i]) + totalPrice
    print("Total price :", totalPrice, "THB")

while True:
    menuName = input("Enter menu : ")
    if(menuName.lower() == 'exit'):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()