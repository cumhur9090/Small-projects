from random import randint


t = ["Rock", "Paper", "Scissors"]



computer = t[randint(0,2)]




player = False


while player == False:
    player = input(f"Rock, Paper, Scissors:\n")
    if player == "exit":
        break
    print(f"Shoot!\nComputer: {computer}")
    if player == computer:
       print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("The computer wins!")
        elif computer == "Scissors":
            print("You win!")
    elif player == "Paper":
       if computer == "Scissors":
           print("The computer wins!")
       elif computer == "Rock":
           print("You win!")
    if player == "Scissors":
        if computer == "Rock":
            print("The computer wins!")
        elif computer == "Paper":
            print("You win!")
    computer = t[randint(0, 2)]
    player = False
