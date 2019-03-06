#1
class MyClass:
    def __init__(self):
        print('Hello world!')

mc=MyClass()

#2
class MyClass:
    def __init__(self, a):
        print('Hello world!')
        print('a = %d' % a)

mc=MyClass(5)

#3
class MyClass:
    a = 0
    b = 0
    c = 0
    def __init__(self):
        print('Hello world!')
    def getdata(self, x, y):
        self.a = x
        self.b = y
    def addnumbers(self):
        self.c = self.a + self.b
    def print_sum(self):
        print('sum = %d' % self.c)

mc=MyClass()
mc.getdata(3,4)
mc.addnumbers()
mc.print_sum()

#4
class MyNewClass(MyClass):
    def __init__(self):
        print('Hello New Class!')
    def print_message(self):
        print('My New Class')

mc=MyNewClass()
mc.getdata(3,4)
mc.addnumbers()
mc.print_sum()
mc.print_message()
