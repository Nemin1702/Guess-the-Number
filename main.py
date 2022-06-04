import random
number=random.randint(1,100)
name=input("What is your name?")
no_of_guesses=0
print("Ok,", name ,", Guess a number from 1-100!")
while no_of_guesses < 5:
    guess=int(input())
    no_of_guesses+=1
    if guess<number:
        print("Your number needs to be higher")
    elif guess>number:
        print("Your number needs to be lower")
    else:
        break
if guess==number:
    print("You have guess the number in " ,str (no_of_guesses), "turns!")
else:
    print("You failed to guess the number. The number was", str (number),"!")