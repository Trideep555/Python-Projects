import random


def comp_choice():
    ch = random.randint(1, 3)
    if ch == 1:
        return "Rock"
    elif ch == 2:
        return "Paper"
    else:
        return "Scissors"


def user_choice():
    ch = input("Enter Rock Paper Scissiors")
    ch = ch[0].upper() + ch[1:]
    if ch in ('Rock', 'Paper', 'Scissors'):
        return ch
    else:
        print("Wrong Choice Try again Please !!")
        user_choice()


def result(score_user, score_comp):
    print("Current Score is")
    print("Computer=", score_comp)
    print("User=", score_user)


winner = ""
score_comp = 0
score_user = 0
play = "Yes";
while play != "No":
    comp = comp_choice()
    user = user_choice()
    print("Computer Entered", comp)
    print("User Entered", user)
    if (user == "Rock") and (comp == "Scissors"):
        winner = "user"
    elif (user == "Scissors") and (comp == "Paper"):
        winner = "user"
    elif (user == "Paper") and (comp == "Rock"):
        winner = "user"
    elif user == comp:
        winner = "Tie"
    else:
        winner = "comp"
    i = 0
    if winner == "user":
        print("Congratulations!! You Won")
        score_user += 1
        result(score_user, score_comp)
    elif winner == "Tie":
        print("Its a Tie!!")
        result(score_user, score_comp)
    else:
        print("Oh! No You lost")
        score_comp += 1
        result(score_user, score_comp)
    print("Wanna Play Again?")
    while i != -1:
        play = input("Say Yes to play again and No to Stop ")
        play = play[0].upper() + play[1:]
        if play not in ('Yes', 'No'):
            print("Sorry Wroing Answer")
        else:
            i = -1
print("Final Score is:-")
print("Computer=", score_comp)
print("User=", score_user)
print("Thank You for playing!!")
