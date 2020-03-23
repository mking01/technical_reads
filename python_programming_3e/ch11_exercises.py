# Ch. 11 - Data Collections

# True / False
# 1. F
# 2. T (from the mean, otherwise is variance if is around the mean)
# 3. F
# 4. F
# 5. F
# 6. F
# 7. T
# 8. T
# 9. F


# Multiple Choice
# 1. B
# 2. B
# 3. D
# 4. C
# 5. D
# 6. A
# 7. D
# 8. D
# 9. C
# 10. B

# Discussion
# 1. Given the initial statements
# s1 = [2,1,4,3]
# s2 = ['C','a','b']
# Show the result of evaluating each sequence:
# a. print(s1 + s2)  # [2, 1, 4, 3, 'C', 'a', 'b']
# b. print(3 * s1 + 2 * s2) # [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'C', 'a', 'b', 'C', 'a', 'b']
# c. print(s1[1])  # 1
# d. print(s1[1:3]) # [1, 4]
# e. print(s1 + s2[-1]) #can only concatenate list, not str to list

# 2. Given the same lists, show values after executing each of the below
# s1 = [2,1,4,3]
# s2 = ['C','a','b']
# a. print(s1.remove(2)) # none
# b. print(s1.sort()) # none
# c. print(s1.append([s2.index('b')])) # none
# d. print(s2.pop(s1.pop(2)))  #index error: pop out of range
# e. print(s2.insert(s1[0], 'd')) # none

# Exercises
# 1. Modify the statistics program from this chapter so that client programs
# have more flexibility computing the mean or standard deviation.
# add functions for mean(nums), StdDev(nums), and meanStdDev(nums) - returns both
# import math
#
#
# def getNumbers():
#     nums = []
#     xStr = input("Enter a number (<Enter> to quit) >>")
#     while xStr != "":
#         x = float(xStr)
#         nums.append(x)
#         xStr = input("Enter a number (<Enter> to quit) >>")
#     return nums
#
#
# def mean(nums):
#     total = 0.0
#     for num in nums:
#         total = total + num
#     return total / len(nums)
#
#
# def stdDev(nums, xbar):
#     sumDevSq = 0.0
#     for num in nums:
#         dev = xbar - num
#         sumDevSq = sumDevSq + dev * dev
#     return math.sqrt(sumDevSq / (len(nums) - 1))
#
#
# def meanStdDev(nums):
#     # calculate mean
#     total = 0.0
#     for num in nums:
#         total = total + num
#     xbar = total / len(nums)
#
#     # use to calculate SD
#     sumDevSq = 0.0
#     for num in nums:
#         dev = xbar - num
#         sumDevSq = sumDevSq + dev * dev
#     sd = math.sqrt(sumDevSq / (len(nums) - 1))
#
#     # return both
#     return xbar, sd
#
#
# def main():
#     print("This program gets the mean and standard deviation, then validates it")
#     data = getNumbers()
#     xbar = mean(data)
#     sd = stdDev(data, xbar)
#     xbar_check, sd_check = meanStdDev(data)
#     print('The mean is', xbar)
#     print('The standard deviation is', sd)
#     print('Function calculating both, mean and sd', xbar_check, ',', sd_check)
#
#
# if __name__ == '__main__': main()

# 5. Most languages do not have the flexible built-in list (array) operations that Python has.  Write
# an algorithm for each of the following Python operations and test your algorithm by writing it
# up in a suitable function.  For example, as a function reverse(myList) should do the same as myList.reverse().
# You cannot use the corresponding Python method to implement your function.

# a. count(myList, x) like myList.count(x)
# myList = ['a', 'a', 'b', 'c', 'c', 'c']
# def count_lst_item(myList, item):
#     # ensure item is in list
#     lst_unique = set(myList)
#
#     lst_common = [x for x in lst_unique if x == item]
#
#     if len(lst_common) == 0:
#         return print("Item does not appear in list.")
#     else:
#         total = 0
#         for i in myList:
#             if i == item:
#                 total = total + 1
#         return print(total)
# tests:
# count_lst_item(myList, 'd') # Item does not appear in list.

# count_lst_item(myList, 'a') # 2


# b. isin(myList, x) like x in myList

# myList = ['a', 'a', 'b', 'c', 'c', 'c']

# def is_in_list(myList, x):
#     unique_items = set(myList)
#     total = 0
#     for i in unique_items:
#         if i == x:
#             total = total + 1
#         else:
#             total = total + 0
#
#     if total > 0:
#         return print(total),print("Yes, item appears in the list.")
#     else:
#         return print(total), print("No, item does not appear in the list.")

# testing:
# is_in_list(myList, 'd') # No, item does not appear in the list.
# is_in_list(myList, 'a') # Yes, item appears in the list.



myList = ['a', 'a', 'b', 'c', 'c', 'c']