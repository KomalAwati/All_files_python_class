#Encapsulation
class Circle:
    def __init__(self, radius):
        # private attribute. It is for internal use only
        # You are not suppose to access this attribute directly or change the value
        # You will be able to do it.. but you should not do it.
        # If you do it, then you might end up screwing up something
        self.radius = radius
    
    # Getter
    @property
    def radius(self):
        print("Getting...")
        return self._radius
    
    # Setter
    @radius.setter
    def radius(self, value):
        print("Setting...")
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        self._radius = value

    def circumference(self):
        return 2 * 3.14 * self._radius

#O/p
'''
c = Circle(20)
Setting...

c.radius
Getting...
20

c.radius
Getting...
20
c.__dict__
{'_radius': 20}
'''
