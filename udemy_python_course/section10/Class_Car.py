
'''
Each set and get method has 'self' in it. Kinda like java when we say 'this'
'''


class Car:

    def __init__(self, type, model, price, milesDrive, owner):
        self._Type = type
        self._Model = model
        self._Price = price
        self._MilesDrive = milesDrive
        self._Owner = owner

    def SetType(self, type):
        self._Type = type

    def GetType(self):
        return self._Type

    def SetModel(self, model):
        self._Model = model

    def GetModel(self):
        return self._Model

    def SetPrice(self, price):
        self._Price = price

    def GetPrice(self):
        return self._Price

    def SetMilesDrive(self, milesDrive):
        self._MilesDrive = milesDrive

    def GetMilesDrive(self):
        return self._MilesDrive

    def SetOwner(self, owner):
        self._Owner = owner

    def GetOwner(self):
        return self._Owner

    def GetCurrentPrice(self):
        return self._Price - (self._MilesDrive*10)


def main():
    myCar = Car("Ford", "F150", 35000, 20, "Julio")

    # calculate the new price of the vehicle
    CurrentPrice = myCar.GetCurrentPrice()
    print("New price of the vehicle is: {}".format(CurrentPrice))


if __name__ == "__main__":
    main()
