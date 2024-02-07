'''
CS 115, Lab 12, Inheritance

Author: Anthony Rizzuto
Pledge: I pledge my honor that I have abdied by the Stevens Honor System.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''

    def __init__(self, make, model, mpg, tank_capacity):
        '''constructor that intializes a Car object and assigns it the values of make, model, mpg,
        and tank capacity '''
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity


    '''Write getters for make, model, mpg, and tank_capacity.'''

    def get_make(self):
        '''gets make of car'''
        return self.__make

    def get_model(self):
        '''gets model of car'''
        return self.__model

    def get_mpg(self):
        '''gets mpg of car'''
        return self.__mpg

    def get_tank_capacity(self):
        '''gets tank capacity of car'''
        return self.__tank_capacity

    '''Write setters for mpg and tank_capacity.'''

    def set_make(self, x):
        '''sets make of car to x'''
        self.__make = x
    
    def set_model(self, x):
        '''sets model of car to x'''
        self.__make = x

    def set_mpg(self, x):
        '''sets mpg of car to x'''
        self.__mpg = x

    def set_tank_capacity(self, x):
        '''sets tank capacity to x'''
        self.__tank_capacity = x

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''

    def get_total_range(self):
        '''Calculates total range a car can drive'''
        return self.__mpg * self.__tank_capacity

    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''

    def __init__(self, make, model, mpg, tank_capacity, __battery_kWh, __miles_per_kWh):
        '''constructor that intializes a Hybrid Car object by inheriting Car class and
        assigns it the existing values of (make, model, mpg, and tank capacity) and new values
        battery kWh and miles per kWh '''
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh = __battery_kWh
        self.__miles_per_kWh = __miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.__battery_kWh * self.__miles_per_kWh

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''

    def get_total_range(self):
        '''returns total range of a hybrid car, battery range combined with gas range'''
        return super().get_total_range() + self.get_battery_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
