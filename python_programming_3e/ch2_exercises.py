# Ch. 2: Writing Simple Programs

# True / False
#
# 1. F
# 2. T
# 3. F
# 4. T
# 5. F
# 6. T
# 7. T
# 8. F
# 9. T
# 10. F

# Multiple Choice
# 1. C
# 2. A
# 3. D
# 4. C
# 5. B
# 6. B
# 7. B
# 8. D
# 9. A
# 10. D

# Discussion
# 1. Software development process, to be followed in order:
#a. Analyze the problem - understand the problem as much as possible.  Can't solve something that's not defined or fully understood.
#b. Determine specifications - describe what your program will do, be sure to talk through all edge cases and what should be included/exlcuded.  Define all parameters.
#c. Create a design - formulate overall structure.  Pseudocode is your friend!!
#d. Implement design - Convert pseudo code into actual code.
#e. Debug / Test - Validate code works as expected, make updates as needed if/when not
#f. Maintain - Continually update program to handle changes to edge cases and parameters and ensure code compatibility with future package changes

# 2. Completed manually

#3. Explain the relationships among the concepts: definite loop, for loop, counted loop.
#a. Definite loop - Simplest kind, will repeat a certain number of times and that number of times is known in advance (not dynamic)
#b. For loop - Loop that iterates based on the index of items in a collection (for i in us_states could repeat 50 times for example)
#c. Counted loop - Loop that continues for a certain number of times, usually defined by range(n)

#4. Show output for all of the below.
#a. for i in range(5):
    #print (i * i)

#a output:
# 0
# 1
# 4
# 9
# 16

#b. for d in [3, 1, 4, 1, 5]:
#    print(d, end=" ")

#b output: 3 1 4 1 5
# Programming Exercises

#c. for i in range(4):
#    print("Hello")

#c output: Hello
#Hello
#Hello
#Hello

#d. for i in range(5):
#    print(i, 2**i)

#d output:
# 0 1
# 1 2
# 2 4
# 3 8
# 4 16

#5. It's a good idea because it makes you think through your logic prior to implementing the logic in code form.  Can also facilitate easy review of your process by someone else.

#6. "sep" separates items printed with whatever character is subbed.  Ex. sep = "," would separate items with a ","

#7. It would print "start" and "end".  The loop would exit the first time because the range is set at (0) and range is not inclusive.

# Programming Exercises
#1. Modify convert.py to include an explanation
# def main():
#     print("This program converts degrees Celsius to degrees Fahrenheit.")
#     celsius = eval(input("What is the Celsius temperature? "))
#     fahrenheit = 9/5 * celsius + 32
#     print("The temperature is", fahrenheit, "degrees Fahrenheit.")
# main()

#2.  Add an input statement at the end of the program so it gives the user a chance to read results before the program quits.
# def main():
#     print("This program converts degrees Celsius to degrees Fahrenheit.")
#     celsius = eval(input("What is the Celsius temperature? "))
#     fahrenheit = 9/5 * celsius + 32
#     print("The temperature is", fahrenheit, "degrees Fahrenheit.")
#     input("Press the <Enter> key to quit.")
# main()

#3. Modify the below to take the average of 3 exam scores.
# def main():
#     print("This program computes the average of 3 exam scores.")
#
#     score1, score2, score3 = eval(input("Enter three exam scores separated by a comma: "))
#     average = (score1 + score2 + score3) / 3
#
#     print("The average of the scores is: ", average)
# main()

#4. Modify the below with a loop so it executes 5x before quitting.  Each time through the loop, the program should get a new temperature and print the converted value.
# def main():
#     print("This program converts degrees Celsius to degrees Fahrenheit.")
#     for i in range(5):
#         celsius = eval(input("What is the Celsius temperature? "))
#         fahrenheit = 9/5 * celsius + 32
#         print("The temperature is", fahrenheit, "degrees Fahrenheit.")
# main()

#5. Modify the below so it computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0 to 100 C.
# def main():
#     print("This program converts degrees Celsius to degrees Fahrenheit.")
#     for i in range(0,110,10):
#         celsius = i
#         fahrenheit = 9/5 * celsius + 32
#         print("Celsius temperature:", celsius, "| Fahrenheit temperature:", fahrenheit)
# main()

#Output:
# This program converts degrees Celsius to degrees Fahrenheit.
# Celsius temperature: 0 | Fahrenheit temperature: 32.0
# Celsius temperature: 10 | Fahrenheit temperature: 50.0
# Celsius temperature: 20 | Fahrenheit temperature: 68.0
# Celsius temperature: 30 | Fahrenheit temperature: 86.0
# Celsius temperature: 40 | Fahrenheit temperature: 104.0
# Celsius temperature: 50 | Fahrenheit temperature: 122.0
# Celsius temperature: 60 | Fahrenheit temperature: 140.0
# Celsius temperature: 70 | Fahrenheit temperature: 158.0
# Celsius temperature: 80 | Fahrenheit temperature: 176.0
# Celsius temperature: 90 | Fahrenheit temperature: 194.0
# Celsius temperature: 100 | Fahrenheit temperature: 212.0

#6. Update the below program so a user can enter a variable number of years.
# def main():
#     print("This program calculates the future value of an investment.")
#
#     principal = eval(input("Enter the initial principal: "))
#     apr = eval(input("Enter the annual interest rate: "))
#     term_years = eval(input("Enter the number of years invested: "))
#
#     for i in range(term_years):
#         principal = principal * (1 + apr)
#         print("The value in year", i + 1, "is:", round(principal,2))
# main()

#7. Update the program in 6 to show total accumulation (I did this in 6).

#8. As an alternative to APR, interest accrued is often described as a nominal rate and number of compounding periods.
# Modify the above to use this method of entering the interest rate.
# def main():
#     print("This program calculates the future value of an investment.")
#
#     principal = eval(input("Enter the initial principal: "))
#     rate = eval(input("Enter the annual interest rate: "))
#     periods = eval(input("Enter the number of times interest is compounded annually: "))
#     term_years = eval(input("Enter the number of years invested: "))
#
#     nominal_rate = rate / periods
#
#     for i in range(periods * term_years):
#         principal = principal * (1 + nominal_rate)
#     print("The value in year", term_years, "is:", round(principal,2))
# main()

#9. Write a program that converts F to celsius.
# def main():
#     print("This program converts fahrenheit to celsius.")
#     fahrenheit = eval(input("Enter temperature in fahrenheit:"))
#     celsius = (fahrenheit - 32) * 5/9
#     print(fahrenheit,"fahrenheit is equivalent to",round(celsius,2),"celsius.")
# main()

#10. Write a program that converts kilometers to miles.  1 km = .62m.
# def main():
#     print("This program converts km to miles.")
#     km = eval(input("Enter distance in km to convert to miles:"))
#     miles = km * .62
#     print(km,"km is equivalent to",miles,"miles.")
# main()

#11. skip

#12. Write an interactive calculator program.  Program should allow user to type a mathematical expression then print the value of the expressoin.
#Include a loop so the user can make as many calculations as they want.
#
# def main():
#     print("Interactive calculator program.  Enter calc below.")
#
#     for i in range(5):
#         calculation = eval(input(""))
#         print(calculation)
#
# main()