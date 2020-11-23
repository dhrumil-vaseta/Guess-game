from random import randint

value = randint(0,10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Hint: 0 - 10 | Guess: "))
    guess_count += 1
    if guess == value:
        print("You won!")
        print(f"Secret number was {value}!")
        break
else:
    print("Out of guesses :(")
    print(f"Secret number was {value}!")