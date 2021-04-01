class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Jirat"
customer1.lastname = "Srialkum"
customer1.addCart()

customer2 = Customer()
customer2.name = "Boom"
customer2.lastname = "S"
customer2.addCart()

customer3 = Customer()
customer3.name = "Jira"
customer3.lastname = ""
customer3.addCart()

customer4 = Customer()
customer4.name = "Ji"
customer4.lastname = "Sri"
customer4.addCart()