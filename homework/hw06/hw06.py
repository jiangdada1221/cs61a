# Object Oriented Programming
#>>> ten, twenty, thirty = 10, 'twenty', [30]   format method
#>>> '{0} plus {1} is {2}'.format(ten, twenty, thirty)
#'10 plus twenty is [30]'
class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            a = Fib(1)
            a.value2 = 0 #value2 tracks the previous number
            return a
        else:
            a = Fib(self.value + self.value2)
            a.value2 = self.value
            return a

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,type,price):
        self.balance = 0
        self.stock = 0
        self.type = type
        self.price = price
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.balance)
        else:
            self.balance,a = 0,self.balance - self.price
            self.stock -= 1
            if a == 0:
                return "Here is your {0}.".format(self.type)
            return "Here is your {0} and ${1} change.".format(self.type,a)
    def deposit(self,amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            self.balance += amount
            return 'Current balance: ${0}'.format(self.balance)
    def restock(self,amount):
        self.stock += amount
        return 'Current {0} stock: {1}'.format(self.type,self.stock)
