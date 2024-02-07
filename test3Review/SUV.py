class Automobile:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def set_make(self, newMake):
        self.__make = newMake

    def set_model(self, newModel):
        self.__model = newModel

    def set_price(self, newPrice):
        self.__price = newPrice

    def __gt__(self, other):
        return self.__price > other.__price

    def __le__(self, other):
        return self.__price <= other.__price

    def __str__(self):
        return self.__make + " " + self.__model

class SUV(Automobile):
    def __init__(self, make, model, price, pass_cap):
        Automobile.__init__(self, make, model, price)
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap

    def set_pass_cap(self, p):
        self.__pass_cap = p

    def __str__(self):
       return self.get_make() + " " + self.get_model()+ " " +str(self.__pass_cap)

    
    
