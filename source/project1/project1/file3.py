import random

number = (random.randint(1, 10))
print("Welcome to the number guessing game I will choose a number between one and ten and you will try and guess it,"
      " good luck!")
while True:
    print('Guess a number between 1 and 10')
    guess = input()
    i = int(guess)
    if i == number:
        print("Good job you guessed it right!!")
        break
    elif i < number:
        print("Sorry your guess is too low.")
    elif i > number:
        print("Sorry your guess is too high.")
