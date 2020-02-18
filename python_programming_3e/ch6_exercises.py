# Ch. 6 - Defining Functions

# True / False
# 1. F
# 2. F
# 3. T
# 4. F
# 5. T #https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
# 6. F
# 7. F
# 8. T
# 9. T
# 10. F

# Multiple Choice
# 1. B
# 2. A
# 3. A
# 4. B
# 5. D
# 6. A
# 7. D
# 8. A
# 9. D
# 10. A

# Discussion
# 1. 2 motivations are making code easily readable and making code easily maintainable.
# 2. Yes

# 3.
# a. Allow you to modify a piece of your function between calls
# b. Formal parameter = default parameter assigned when the function is defined.  Actual parameter = what's actually passed.
# c. Function parameters have the same scope as local variables.  Difference is function parameters are initialized only when the function is called.

# 4.
# a. Through parameters
# b. Through returns

# 5.
# a. return cubed x
# b.
# c. Because answer is an ordinary variable assigned outside the function

# def cube(x):
#     answer = x * x * x
#     return answer
#
#
# answer = 4
# result = cube(3)
# print(answer, result)

# Exercises
# 1. Write a program to print out lyrics for 5 different animals for "Old Macdonald."

# animals_dict = {"cow": "moo", "duck": "quack", "sheep": "bah", "dog": "woof", "mouse": "squeak"}
#
#
# def has_farm():
#     return "Old MacDonald had a farm, ee-igh, ee-igh, oh!\n"
#
#
# def animal_on_farm():
#     return "And on that farm he had a " + animal + ", ee-igh, ee-igh, oh!\n"
#
#
# def sound_here_there_everywhere():
#     return "With a " + animals_dict[animal] + "," + animals_dict[animal] + \
#            " here and a " + animals_dict[animal] + "," + animals_dict[animal] + " there.\n Here a " \
#            + animals_dict[animal] + ", there a " + animals_dict[animal] + \
#            ", everywhere a " + animals_dict[animal] + ", " + animals_dict[animal] + "."
#
#
# def sing_song(animal):
#     lyrics = has_farm() + animal_on_farm() + sound_here_there_everywhere()
#     print(lyrics)
#
#
# for animal in animals_dict.keys():
#     sing_song(animal)