import random

options = ("rock", "paper", "scissors")

playing = True
playerscore = 0
computerscore = 0

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Choose rock paper or scissors: ").lower()

    print(f"You: {player}" )
    print(f"Computer: {computer}")

    if player == computer:
        playerscore += 1
        computerscore += 1
        print("What? It's a tie!")
        print("Computer: I'm winning the next one!")
        print(f"The score is: \n Computer({computerscore}) : You({playerscore})")

    elif player == "scissors" and computer == "paper":
        playerscore += 1
        print("Congratulations you win!")
        print(f"The score is: \n Computer({computerscore}) : You({playerscore})")
    elif player == "rock" and computer == "scissors":
        playerscore += 1
        print("Congratulations you win!")
        print(f"The score is: \n Computer({computerscore}) : You({playerscore})")
    elif player == "paper" and computer == "rock":
        playerscore += 1
        print("Congratulations you win!")
        print(f"The score is: \n Computer({computerscore}) : You({playerscore})")
    else:
        computerscore += 1
        print("You lose!")
        print("Computer: Better luck next time!")
        print(f"The score is: \n Computer({computerscore}) : You({playerscore})")

    repeat = input("Do you want to play again?(y/n): ").lower()
    if repeat == "y" or repeat == "yes":
        print("Game on!")
    else:
        playing = False
        print("Thanks for playing!")