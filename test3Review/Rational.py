class Rational:
    def __init__(self, n, d):
        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        else:
            self.__denominator = d #__ before variable name makes variable private
            self.__numerator = n
            '''
            self._carry = 1 # Single Leading Underscore is for Internal use
            self.def_ = 'Test' # Single Trailing Underscore is to use keywords as variable names
            for _ in range(5): # Underscore by itself shows temporary/insignificant variable
                print('Hello')
            '''

    def get_numerator(self): # Accessor or Getter
        return self.__numerator

    def set_numerator(self, newn): # Mutator of Setter
        self.__numerator = newn
        
    def isZero(self):
        return self.__numerator == 0

    def add(self, other):
        newDenominator = self.__denominator * other.__denominator
        newNumerator = self.__numerator * other.__denominator +\
                       self.__denominator * other.__numerator
        return Rational(newNumerator, newDenominator)

    def __add__(self, other):
        newDenominator = self.__denominator * other.__denominator
        newNumerator = self.__numerator * other.__denominator +\
                       self.__denominator * other.__numerator
        return Rational(newNumerator, newDenominator)

    def __ge__(self, other):
        return self.__numerator * other.__denominator >= self.__denominator * other.__numerator

    def __eq__(self, other):
        return self.__numerator * other.__denominator == self.__denominator * other.__numerator

    def __str__(self):
        return str(self.__numerator)+" / "+str(self.__denominator)

def main():
    r1 = Rational(36, 1000)
    r2 = Rational(6, 1000)
    print("r1 >= r2: ", r1 >= r2)
    print("r1 == r2: ", r1 == r2)

if __name__ == "__main__":
    main()


