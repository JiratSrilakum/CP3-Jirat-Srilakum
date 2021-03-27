menuList = []

def showBill():
    totalPrice = 0
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i])
        totalPrice = totalPrice + int(menuList[i][1])
    print("Total price :",totalPrice)
while True:
    menuName = input("Enter menu : ")
    if(menuName.lower() == 'exit'):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])
showBill()