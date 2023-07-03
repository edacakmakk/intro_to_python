import random

print(('*'*10) + " ROCK PAPER SCİSSORS " + ('*'*10))

choices = ["Rock", "Paper", "Scissors"]

user_score, computer_score = 0, 0

while True:
    user = input("Your choice: ")
    computer = random.choice(choices)
    
    if user == "Rock":
        if computer == "Rock":
            print("Computer choice: Rock so try again")
        elif computer == "Paper":
            print("Computer choice: Paper. You lose!")
            computer_score += 10
        else:
            print("Computer choice: Scissors. You win!")
            user_score += 10
    
    elif user == "Paper":
        if computer == "Rock":
            print("Computer choice: Rock. You win!")
            user_score += 10
        elif computer == "Paper":
            print("Computer choice: Paper so try again")
        else:
            print("computer choice: Scissors. You lose!")
            computer_score += 10

    elif user == "Scissors":
        if computer == "Rock":
            print("Computer choice: Rock. You lose!")
            computer_score += 10
        elif computer == "Paper":
            print("Computer choice: Paper. You win!")
            user_score += 10
        else:
            print("Computer choice: Scissors so try again")
    else:
        print("Wrong information")
        break
    print("\nUser's score: {}\nComputer's score: {}".format(user_score, computer_score))

"""
if bloklarını yok et sondaki puan hesaplamayı düzenle.
"""