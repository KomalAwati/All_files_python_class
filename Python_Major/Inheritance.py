#Single inheritance
'''
class A:
    def feat1(self):
        print("feature of A has been called")
class B(A):
    def feat2(self):
        print("feature of B has been called")

a1 = A()
a1.feat1()

b1= B()
b1.feat1()
b1.feat2()

'''
#Using constructor in inheritance
'''
class M_operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
'''
#Terminal
'''
a = M_operation(2, 3)
a.add()
5
a.sub()
-1
a.mul()
6
a.div()
0.6666666666666666
'''

class Add:
    def __init__(self, a, b):
        self
