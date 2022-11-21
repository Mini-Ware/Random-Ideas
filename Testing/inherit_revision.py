class amogus:
    count = 0
    def __init__(self, color):
        #Class attributes affects all objects derived from that class
        self.__class__.count += 1

        #Private attributes cannot be directly accessed if inherited from parent to child
        #It can only be accessed via accessor and mutator methods
        #self.__color = color

        #Public data can be directly accessed
        self.color = color
    def get_count(self):
        return self.__class__.count
    def get_color(self):
        return self.__color
    def __str__(self):
        return "amogus character"

class red(amogus):
    def __init__(self, color="red"):
        #When using super(), self is not required
        #super().__init__(color)
        amogus.__init__(self, color)
    def __str__(self):
        #This leads to error as it tries to directly access private attributes from parent class
        #return super().__str__()+f"\nMy color is {self.__color}"
        #This will work as the private attribute is accessed through methods
        #return super().__str__()+f"\nMy color is {self.get_color()}"

        #Public data inherited can be directly accessed
        #Using parent method in child method that overrides it is called extending the class
        return super().__str__()+f"\nmy color is {self.color}"

class blue(amogus):
    def __init__(self, color="blue"):
        #When using super(), self is not required
        #super().__init__(color)
        amogus.__init__(self, color)
    def __str__(self):
        #This leads to error as it tries to directly access private attributes from parent class
        #return super().__str__()+f"\nMy color is {self.__color}"
        #This will work as the private attribute is accessed through methods
        #return super().__str__()+f"\nMy color is {self.get_color()}"

        #Public data inherited can be directly accessed
        #Using parent method in child method that overrides it is called extending the class
        return super().__str__()+f"\nmy color is {self.color}"

sussy = red()
imposter = blue()

if isinstance(sussy, amogus):
    print("verified ",end="")
    print(sussy)

#only 1 as child doesn't inherit parent class attributes, they are their own class
print(f"there is currently {amogus.count} amogus(s)")

yellow = amogus("yellow")
purple = amogus("purple")
orange = amogus("orange")

#this works as intended
print(f"there is currently {amogus.count} amogus(s)")
