class Person: #Base class or superclass
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def asleep(self, time):
        return 0 <= time <= 7

    def __str__(self):
        return self.firstName + " " + self.lastName

class Student(Person): # Derived Class or subclass
    def __init__(self, first, last, Id):
        Person.__init__(self, first, last)
        self.ID = Id

    # Comment this out to see which asleep function will run for Student
    def asleep(self, time):
        return 0 <= time <= 3
    
    def __str__(self):
        return Person.__str__(self)+ ", asleep is " + str(self.asleep(2))
