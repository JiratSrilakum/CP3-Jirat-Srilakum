class Vehicle:
    licenCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()