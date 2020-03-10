# Ch. 10 - Defining Classes

# True / False
# 1. True
# 2. False, methods are functions that live inside the object (not instance variables)
# 3. False
# 4. False
# 5. False
# 6. True
# 7. False, docstrings accompany execution whereas comments do not
# 8. False, only true for local function variables, the entire point is they live on beyond the method
# 9. False
# 10. True

# Multiple Choice
# 1. b
# 2. a
# 3. d
# 4. b
# 5. a
# 6. b
# 7. c
# 8. skipped this exercise
# 9. skipped this exercise
# 10. c

# Discussion
# 1.
# instance variable:  Class attribute variable, not accessible if the class object has not been initialized, otherwise always accessible
# regular variable: local, has to be explicitly created and called or otherwise will not exist and cannot be referenced between files, etc.

# 2.  Explain the below in terms of actual code that would be found in a class definition
# a. method - class House
# b. instance variable - house = House()
# c. constructor - def __init__(self, attribute1, attribute2), invoked by calling houses = House()
# d. accessor - house.get_attribute(), accesses existing feature
# e. mutator - house.set_attribute(7), updates or modifies existing feature value

# 3. show the output that would result from below:
# class Bozo:
#     def __init__(self, value):
#         print("Creating a Bozo from:", value)
#         self.value = 2 * value
#
#     def clown(self, x):
#         print("Clowning:", x)
#         print(x * self.value)
#         return x + self.value
#
# def main():
#     print("Clowning around now.")
#     c1 = Bozo(3)
#     c2 = Bozo(4)
#     print(c1.clown(3))
#     print(c2.clown(2))

#main()


# Exercises
# 9. Write a class to represent spheres.  Your class should implement the following:
# __init__
# getradius()
# surfacearea()
# volume

class Spheres:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        self.area = 4 * 3.14 * (self.radius**2)
        return self.area

    def volume(self):
        self.volume = (4/3) * 3.14 * (self.radius**3)
        return self.volume

def main():
    print("Calculating sphere features")
    s1 = Spheres(3)
    print(s1.getRadius())
    print(s1.surfaceArea())
    print(s1.volume())

main()