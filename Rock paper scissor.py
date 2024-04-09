import random
#Rock,paper,scissor.

player=input("Lets play rock, paper, scissor! Say yes or no.")
if player.lower() == "yes":
    print("I'll win!")

else: 
    print("I would have won anyways")
    exit()

try:
    choice = int(input("Enter your choice (5 for Rock, 6 for Paper, 7 for Scissors): "))
    if choice not in [5, 6, 7]:
        raise ValueError("Invalid choice, enter 5, 6, or 7.")

    randomnumber = random.randint(5, 7)

    if choice == randomnumber:
        print("The computer chose..", randomnumber)
        print("It's a tie!")
    elif (choice == 5 and randomnumber == 7) or (choice == 6 and randomnumber == 5) or (choice== 7 and randomnumber == 6):
        print("The computer chose..", randomnumber)
        print("You win!")
    else:
        print("The computer chose..", randomnumber)
        print("Computer wins!")
except ValueError as a:
    print("ValueError:", "a")
except Exception as a:
    print("Error:", "a")