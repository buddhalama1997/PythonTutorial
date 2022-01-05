import random

secretNumber = random.randint(1,20)

for guessTaken in range (1,7):
    print('Take a Guess.')
    guess = int(input())

    if guess < secretNumber:
        print('You guess too low.')
    elif guess > secretNumber:
        print('You guess too high.')
    else:
        break

if guess == secretNumber:
    print('Great Job! You guessed my number in ' + str(guessTaken)+ ' guess.')
else:
    print('Nope. The number I am thinking of was' + str(secretNumber))