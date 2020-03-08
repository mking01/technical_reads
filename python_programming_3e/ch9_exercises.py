# Ch. 9: Simulation

# True / False
# 1. F
# 2. F - float not int
# 3. T
# 4. T
# 5. T
# 6. F
# 7. T / F - one piece at a time, but incrementally as all pieces are built out
# 8. F
# 9. F
# 10. F


# Multiple Choice
# 1. C
# 2. C
# 3. D
# 4. A - function parameters and outputs passed between steps
# 5. C
# 6. A
# 7. B
# 8. A
# 9. A
# 10. A


# Discussion
# 2.
# a. generate a random int between 0 - 10
# from random import randint, seed
#
# seed(10)
#
# #for _ in range(10):
# value = randint(0, 10)
# print(value)
# b. Generate a random float between -0.5 to 0.5
# from random import uniform, seed
#
# seed(10)
# value = uniform(-0.5, 0.5)
# print(value)
# e. A random float in the range -10.0 - 10.0
# from random import uniform, seed
#
# seed(10)
# value = uniform(-10.0, 10.0)
# print(value)

# Exercises
# 1. Revise the racquetball simulation so it computes results for the best of n game matches.
from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print("players, A and B.  The ability of each player is")
    print("indicated by a probability that")
    print("the player wins the point when serving.  Player A")
    print("always has the first serve.")


def getInputs():
    # Returns the simulation parameters
    probA = float(input("What is the prob player A wins a serve?"))
    probB = float(input("What is the prob player B wins a serve?"))
    n = int(input("How many games to simulate?"))
    return probA, probB, n


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose abilities = probability of winning a serve
    # Return number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving == "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False if it is not over (total = 15)
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


if __name__ == "__main__":
    main()

# 2.
# 3.
# 4.
