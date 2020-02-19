# Ch. 7 - Decision Structures

# True / False
# 1. T
# 2. F
# 3. T
# 4. T
# 5. T
# 6. F
# 7. F
# 8. F
# 9. T
# 10. F


# Multiple Choice
# 1. C
# 2. C
# 3. B
# 4. B
# 5. B
# 6. C
# 7. A
# 8. C
# 9. A
# 10. C


# Discussion
# 1.
# a. simple decision: if true then x
# b. two-way decision: if / else
# c. multi-way decision: if / else with nested if else
# 2. Exception handling using try/except is similar to handling cases using ordinary decision structures
# in that both use conditional boolean logic flows to navigate the task structure.  They are different in that
# try/except is based more on values returned than values gleaned within the middle of the process
# try (to run the body, if it evaluates to a # return it) else if value error, throw error (or do something else)
# 3.
# a. 3, 4, 5 -> Trees Larch Done
# b. 3, 3, 3 -> Trees Chestnut Done
# c. 5, 4, 3 -> "Spam Please!" Done
# d. 3, 5, 2 -> Trees Larch Done
# e. 5, 4, 7 -> "It's a late parrot!" Done
# f. 3, 3, 2 -> Trees Larch Done


# Exercises
# 1. Write a program to input number of hours worked and hourly rate and calculate total wages.

# def main():
#     print("This program calculates weekly wages for one worker.")
#
#     hours, wages = eval(input("Enter total weekly hours and hourly rate in this format x, y:"))
#
#     total_pay = 0
#     if hours <= 40:
#         total_pay = hours * wages
#         print(total_pay)
#     else:
#         total_pay = (40 * wages) + ((hours - 40) * (1.5 * wages))
#         print(total_pay)
#
# main()

# 4. A student with less than 7 credits is a freshman, less than 16 = soph, less than 26 - junior.
# def main():
#     print("This program calculates class standing.")
#     hours = eval(input("Number of credit hours earned:"))
#
#     if hours < 7:
#         print("Freshman")
#     elif hours >= 7:
#         if hours < 16:
#             print("Sophomore")
#         elif hours >= 16:
#             if hours < 26:
#                 print("Junior")
#             else:
#                 print("Senior")
# main()

# 5.  Write a program caulcating a person's BMI and return back the status.
# def main():
#     print("This program calculates BMI health.")
#     height, weight = eval(input("Enter height (inches) and weight (pounds): "))
#
#     bmi = round(weight / height)
#
#     if bmi < 19:
#         print("BMI is below healthy range.")
#     elif bmi >= 19:
#         if bmi < 25:
#             print("BMI is in healthy range.")
#         else:
#             print("BMI is above healthy range.")
#
# main()

# 11. Write a program to identify if a year is a leap year.
# def main():
#     print("This program determines if a given year is a leap year.")
#
#     year = eval(input("Enter the year to be evaluated:"))
#     invalid_centuries = (1800, 1900)
#
#     if year % 4 == 0:
#         if year not in invalid_centuries:
#             print(year, "is a leap year.")
#         else:
#             print(year, "is not a leap year.")
#     else:
#         print(year, "is not a leap year.")
#
# main()
