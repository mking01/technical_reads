# Ch. 5: Strings

# True / False
# 1. F
# 2. T
# 3. F
# 4. T
# 5. T
# 6. T
# 7. T
# 8. F
# 9. F
# 10. F
#
# Multiple Choice
# 1. D
# 2. C
# 3. A
# 4. C
# 5. C
# 6. D
# 7. D
# 8. C
# 9. C
# 10. A


# Discussion
#1. Show results of the following expressions:
s1 = 'spam'
s2 = 'ni!'
#
# print("The Knights who say, " + s2)
# print(3 * s1 + 2 * s2)
# print(s1[1])
# print(s1[1:3])
# print(s1[2] + s2[:2])
# print(s1 + s2[-1])
# print(s1.upper())
# print(s2.upper().ljust(4) * 3)

#2. Given the same initial statements, show a python expression that could
# construct each of the following results by performing string operations.

#a. "NI"
#print(s2[0:2].upper())

#b. ni!spamni!
#print(s2 + s1 + s2)

#c. "Spam Ni!" x 3
#print(s1.title() + " " + s2.title())

#d. "spam"
#print(s1)

#e. ["sp", "m"]
# part_1 = s1[0:2]
# part_2 = s1[3]
# end = part_1 + ", " + part_2)
# print(end)

#f. "spm"
#print(s1[0:2] + s1[3])

# Exercises:
#2. A CS professor gives 5 point quizzes on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
# Write a program accepting a quiz score input and outputting a grade.
# print("This program converts quiz scores to grades.")
#
# score = eval(input("Enter quiz score (0-5):"))
#
# scores_grades_dict = {0: "F", 1: "F", 2: "D", 3: "C", 4: "B", 5: "A"}
#
# grade = scores_grades_dict[score]
#
# print("Student with a quiz score of", score, "received a grade of", grade)

#3. A CS professor gives 100 point exams.  Write a program that accepts a score as an input
# and returns the corresponding grade.
# print("This program converts exam scores to grades.")
#
# score = eval(input("Enter exam score (0-100):"))
#
# def get_grade(score):
#     if score < 60:
#         grade = "F"
#     elif score >= 60 and score < 70:
#         grade = "D"
#     elif score >= 70 and score < 80:
#         grade = "C"
#     elif score >= 80 and score < 90:
#         grade = "B"
#     else:
#         grade = "A"
#
#     return grade
#
# grade = get_grade(score)
#
# print("Student with a quiz score of", score, "received a grade of", grade)

#4. Write a program allowing the user to type a phrase and output the acronym for that phrase.
# print("This program converts a phrase to an acronym.")
#
# phrase = input("Enter phrase to convert to acronym:").split(" ")
#
# acronym = []
#
# for word in phrase:
#     word = word.title()
#     acronym.append(word[0])
# print("The acronym for phrase",phrase,"is",acronym)

#9. Write a program to count the number of words in a sentence entered by the user.
# print("This program counts number of words in a sentence.")
#
# sentence = input("Enter sentence:").split(" ")
#
# total = 0
# for word in sentence:
#     total = total + 1
#
# print("The total number of words in the sentence is", total)


#10. Write a program to calculate the average word length in a sentence.

# print("This program calculates average length of words in a sentence.")
#
# sentence = input("Enter sentence:").split(" ")
#
# word_count = 0
# word_length = 0
# for word in sentence:
#     word_count = word_count + 1
#     word_length = len(word) + word_length
#
# avg_len = word_length / word_count
#
# print("The average word length in the sentence is", round(avg_len))









