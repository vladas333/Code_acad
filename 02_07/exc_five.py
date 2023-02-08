#create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
import random


x = random.randint(1, 10)
try_count = 5
ans = 0

while ans < try_count:
    ans += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in ",
            ans, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if ans >= try_count:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")