# Ch. 1 True / False:
# 1. F
# 2. T
# 3. F
# 4. T
# 5. F
# 6. T
# 7. F
# 8. T
# 9. F
# 10. F
#
#
# # Multiple Choice:
# 1. B
# 2. d
# 3. D
# 4. A
# 5. b
# 6. b
# 7. C
# 8. b
# 9. a
# 10. d
#

# Discussion:
# 1a. Hardware - physical components of a computer
# Software - program run within a computer
#
# 1b. algorithm - steps to solve a problem
# program - implementation of the algorithm
#
# 1c. programming language - language that can be understood by machines
# natural language - natural speech
#
# 1d. high level language - language that can be understood by people. must be compiled or interpreted to be understood by a computer
# machine language - language that can only be understood by machines
#
# 1e. interpreter - translates code into machine language line by line
# compiler - translates code into machine language all at once
#
# 1f. syntax - form of program script
# semantics - meaning of program script
#
# 2.  Five basic functional units of a computer and their purposes:
# Input devices - Connect the computer with external world information
# CPU - similar to the brain of the computer, conducts basic operations
# Main memory - ex. RAM, directly accessed by the CPU, stores programs and data
# Secondary memory - ex. HDD or SSD, stores information not needed or able to be held by the main, more permanent storage
# Output devices - Pass output from the computer to the external world

#3.  Algorithm to make PB&J:
# 1. Check to ensure you have ingredients (bread, pb, j).  If not, go to store and get (reference separate program file).
# 2. If you have ingredients, get them from where they are stored.
# 3. Get a knife.
# 4. Get a plate.
# 5. Open bread.  Remove two slices of bread.  Put on plate side by side.
# 6. Open peanut butter. Pick up knife. Spread peanut butter on one slice of bread.
# 7. Repeat step 6 only for jelly.
# 8. Pick up one slice of bread with the topping side facing up.
# 9. Flip slice so topping side is facing down and meets the topping up alternate slice.
# 10. Enjoy sandwich.

# 4. Medicine, finance, anywhere you need to match an exact value rather than a rounded representation or approximation.
#
# 5.
# print("This program illustrates a chaotic function")
# x = eval(input("Enter a number between 0 and 1:"))
# for i in range(10):
#     x = 3.9 * x * (1 - x)
#     print(x)

#Answer:
# 0.49724999999999997
# 0.97497050625
# 0.09517177095121285
# 0.3358450093643686
# 0.8699072422927216
# 0.4413576651876355
# 0.9615881986142427
# 0.14405170611022783
# 0.48087316710014555
# 0.9735732406265619

# Programming Exercises:
#1. :
# print("hello, world")
# print("hello","world")
# print(3)
# print(3.0)
# print(2 + 3)
# print(2.0 + 3.0)
# print("2" + "3")
# print("2 + 3 =", 2 + 3)
# print(2 * 3)
# print(2 ** 3)
# print(7 / 3)
# print(7 // 3)
#
# #Answers:
# hello, world
# hello world
# 3
# 3.0
# 5
# 5.0
# 23
# 2 + 3 = 5
# 6
# 8
# 2.3333333333333335
# 2

# #2.
# print("This program illustrates a chaotic function")
# x = eval(input("Enter a number between 0 and 1:"))
# for i in range(10):
#     x = 3.9 * x * (1 - x)
#     print(x)

# 0.17:
# 0.5502900000000001
# 0.9651365720099999
# 0.13122708057726604
# 0.4446254822116916
# 0.963041284840878
# 0.13881179727834456
# 0.4662180206373313
# 0.9705492336943269
# 0.1114753328117588
# 0.38628947364643895


# 0.16:
# 0.52416
# 0.97272354816
# 0.10347654335857881
# 0.361799678499242
# 0.9005126174346398
# 0.34939960877504994
# 0.8865461364352788
# 0.39227012918713944
# 0.9297376722451131
# 0.254769578908072

#4:
# print("This program illustrates a chaotic function")
# x = eval(input("Enter a number between 0 and 1:"))
# for i in range(20):
#     x = 3.9 * x * (1 - x)
#     print(x)

#5:
# print("This program illustrates a chaotic function")
# x = eval(input("Enter a number between 0 and 1:"))
# n = eval(input("How many numbers should I print?"))
# for i in range(n):
#     x = 3.9 * x * (1 - x)
#     print(x)

# 6.
# print("This program illustrates a chaotic function")
# x = eval(input("Enter a number between 0 and 1:"))
#
# a = x
# b = x
# c = x
#
# print("V1: 3.9 * x * (1 - x):")
# for i in range(10):
#     a = 3.9 * a * (1 - a)
#     print(a)
#
# print("V2: 3.9 * (x - x * x):")
# for i in range(10):
#     b = 3.9 * (b - b * b)
#     print(b)
#
# print("V3: 3.9 * x - 3.9 * x * x:")
# for i in range(10):
#     c = 3.9 * c - 3.9 * c * c
#     print(c)

# Answer for x = 0.16
# V1: 3.9 * x * (1 - x):
# 0.52416
# 0.97272354816
# 0.10347654335857881
# 0.361799678499242
# 0.9005126174346398
# 0.34939960877504994
# 0.8865461364352788
# 0.39227012918713944
# 0.9297376722451131
# 0.254769578908072
# V2: 3.9 * (x - x * x):
# 0.52416
# 0.9727235481600001
# 0.10347654335857843
# 0.36179967849924083
# 0.9005126174346385
# 0.34939960877505405
# 0.8865461364352836
# 0.39227012918712506
# 0.929737672245101
# 0.2547695789081125
# V3: 3.9 * x - 3.9 * x * x:
# 0.52416
# 0.9727235481600001
# 0.10347654335857825
# 0.3617996784992403
# 0.9005126174346378
# 0.34939960877505616
# 0.886546136435286
# 0.3922701291871178
# 0.9297376722450948
# 0.254769578908133

# 7. Modify to accept two inputs
# print("This program illustrates a chaotic function")
# x, y = eval(input("Enter 2 numbers between 0 and 1:"))
#
# print("V1: 3.9 * x * (1 - x):")
# for i in range(10):
#     x = 3.9 * x * (1 - x)
#     print(x)
#
# print("V2: 3.9 * y * (1 - y):")
# for i in range(10):
#     y = 3.9 * y * (1 - y)
#     print(y)

# Answer: (x = 0.16, y = 0.17)
# V1: 3.9 * x * (1 - x):
# 0.52416
# 0.97272354816
# 0.10347654335857881
# 0.361799678499242
# 0.9005126174346398
# 0.34939960877504994
# 0.8865461364352788
# 0.39227012918713944
# 0.9297376722451131
# 0.254769578908072
# V2: 3.9 * y * (1 - y):
# 0.5502900000000001
# 0.9651365720099999
# 0.13122708057726604
# 0.4446254822116916
# 0.963041284840878
# 0.13881179727834456
# 0.4662180206373313
# 0.9705492336943269
# 0.1114753328117588
# 0.38628947364643895
