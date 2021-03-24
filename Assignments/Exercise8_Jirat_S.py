usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == 'admin' and passwordInput == '000':
    print("Welcome to B Restaurant")
    print("-----------------------")
    print("         Menu          ")
    print("1.Ribeye steak : 150 THB")
    print("2.Salmon steak : 120 THB")
    print("3.Chicken steak : 100 THB")
    print("4.Pork black pepper steak : 110 THB")
    print("5.Saba steak : 130 THB")
    print("6.Lamb steak : 160 THB")
    userSelected = int(input("Choose : "))
    numberOfSteak = int(input("Amount : "))
    if userSelected == 1:
        print("Ribeye steak :",numberOfSteak,"->","Total",150 * numberOfSteak,"THB")
    elif userSelected == 2:
        print("Salmon steak :",numberOfSteak,"->","Total",120 * numberOfSteak,"THB")
    elif userSelected == 3:
        print("Chicken steak :", numberOfSteak,"->","Total",100 * numberOfSteak, "THB")
    elif userSelected == 4:
        print("Pork black pepper steak :", numberOfSteak,"->","Total",110 * numberOfSteak, "THB")
    elif userSelected == 5:
        print("Saba steak :", numberOfSteak,"->","Total",130 * numberOfSteak, "THB")
    elif userSelected == 6:
        print("Lamb steak :", numberOfSteak,"->","Total",160 * numberOfSteak, "THB")

