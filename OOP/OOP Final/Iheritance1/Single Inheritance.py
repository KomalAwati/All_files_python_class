#inheritance - (Is a relationship)
#In OO programming, the concepts of IS-A is a totally based on inheritance.
#Which can be of type Class inheritance

#It is just like saying "A is a B type of thing"
#Eg. Apple is a fruit #Car is a Vehicle etc

#Inheritance is a unidirectional. For eg. House is Building but, Building is not a house



class Date:
    def get_date(self):
        print("2016-05-14")


class Time(Date):
    def get_time(self):
        print("07:00:00")


# Creating an instance from `Date`
dt = Date()
dt.get_date()  # Accesing the `get_date()` method of `Date`
print("--------")

# Creating an instance from `Time`.
tm = Time()
tm.get_time()  # Accessing the `get_time()` method from `Time`.
# Accessing the `get_date() which is defined in the parent class `Date`.
tm.get_date()


#O/p -
'''
2016-05-14
--------
07:00:00
2016-05-14
'''
