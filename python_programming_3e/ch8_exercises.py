# Ch. 8: Loops and Booleans

# True / False
# 1. F
# 2. T
# 3. F
# 4. T
# 5. T
# 6. T #F?
# 7. T
# 8. T
# 9. F
# 10. T



# Multiple Choice
# 1. A
# 2. C
# 3. D
# 4. B
# 5. C
# 6. A
# 7. D
# 8. B
# 9. C
# 10. B


# Discussion
# 1.
# a. definite loop - usually does not use while, has a clear end
# a. indefinite loop - usually uses a while, which risks creating an indefinite loop with no break point
# b. for loop - iterative, may require more code but usually is slightly more clear, less risk of indavertently creating indefinite loops
# b. while loop - while condition is met, do something.  Can be more explicit (less code) but risk creating an infinite loop in the process
# c. interactive loop - dynamically accepts inputs while running the loop (e.g. iteratively input 5 values)
# c. sentinel loop - runs until the pre-defined sentinel number or value is passed (e.g. exit upon inputting -1 or a blank string)
# d. end of file loop - loop and a half, checks the output of the loop
# 3.
# a.
# total = 0
# while i < (n + 1):
#     total = total + i
#
# # b.
# total = 0
# while i < (n + 1):
#     if i % 2 != 0:
#         total = total + i
#
# # c. Sum a series of numbers entered by the user until 999 is entered.
#
# user_numbers_list = [1, 2, 3, 4]
#
# total = 0
#
# for i in user_numbers_list:
#     while i != 999:
#         total = total + i
#     else:
#         break

# Exercises
# 1. Write a program that computes and outputs the nth Fib number where n is a user-ented value.
# def main():
#     print("This program computes the nth Fibonacci number in a sequence.")
#
#     n = eval(input("Enter the nth Fibonacci number:"))
#
#     #def Fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return print(((n - 1) + (n - 2)))
#
# main()

# 7. Get a user entered number, check to make sure it is even, then find 2 prime numbres that sum to the number
# def main():
#     print("This program finds primes summing to n.")
#
#     n = eval(input("Enter even number:"))
#
#     while n % 2 == 0:
#         ### Find primes
#         ### Check to see if they sum to n
#     else:
#         print("Number is not even.  Pick a new number.")