systemMenu = {"Pork":35,"Fish":40,"Chicken":45,"Beef":55}
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
        menuList.append([menuName,systemMenu[menuName]])
showBill()