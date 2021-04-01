import random
guess=int(input("Guess a number : "))
win_number=random.randint(1,6)
game_end=True
while game_end:
    if guess==win_number:
        print("You Win !!")
        game_end=False
    else:
        if guess>win_number:
            print("Too High !")
        else:
            print("Too Low !")
        guess=int(input("Guess aggain : "))