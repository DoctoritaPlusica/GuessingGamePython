import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    guess_counter=0
    while guess !=random_number: #and guess_counter<5:
        guess=int(input(f"Guess a number between 1 and {x}"))
        if guess<random_number:
            print("sorry , too low ")
        elif guess>random_number:
            print("sorry too high ")
        else:
            print("You guessed corect")
            break
        guess_counter += 1
        if guess_counter<5:
            print(f"you have {5 - (guess_counter)} guesses left")
        else:
            print(f"Out of guesses , the number was {random_number}")
            break


guess(5)