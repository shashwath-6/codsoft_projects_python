import random

val = random.randint(1, 3)
"""ITS THE VARIABLE WHICH CONTAINS THE COMPUTER CHOICE CREATED BY SHASHWATH M"""
def game():
    """IT'S A FUNCTION WHICH EXECUTED THE ROCK PAPER SCISSORS GAME CREATED BY SHASHWATH M
    VALUE_TAKES -> INT  VALUE_RETURN -> STRING """
    points_user = 0
    """IT RETURNS OR STROE THE POINTS OF THE USER CREATED BY SHASHWATH M VAL ->INT"""
    points_comp = 0
    """IT RETURNS OR STORE THE POINTS OF THE USER CREATED BY SHASHWATH M"""
    for i in range(0, turns):
        rock_paper_scissor = ""
        """ITS A STRING WHICH CONTAINS THE VALUE FOR THE COMPUTER CHOICE CREATED BY SHASHWATH M VAL->INT"""
        if val == 1:
            rock_paper_scissor = "rock"
        if val == 2:
            rock_paper_scissor = "paper"
        if val == 3:
            rock_paper_scissor = "scissor"
        #print(rock_paper_scissor)
        #print(val)
        user_val = int(input("Enter your choice: "))
        """ITS A CHOICE OF A USER CREATED BY SHASHWATH M"""
        if user_val == 1:
            if rock_paper_scissor == "rock":
                print("It's a tie!")
                points_user += 1
                points_comp += 1
            if rock_paper_scissor == "paper":
                print("YOU LOSE")
                points_comp += 1
            if rock_paper_scissor == "scissor":
                print("YOU WON")
                points_user += 1
        if user_val == 2:
            if rock_paper_scissor == "rock":
                print("YOU WON")
                points_user += 1
            if rock_paper_scissor == "paper":
                print("IT'S A TIE!")
                points_comp += 1
                points_user += 1
            if rock_paper_scissor == "scissor":
                print("YOU LOSE!")
                points_comp += 1
        if user_val == 3:
            if rock_paper_scissor == "rock":
                print("YOU LOSE!")
                points_comp += 1
            if rock_paper_scissor == "paper":
                print("YOU WON!")
                points_user += 1
            if rock_paper_scissor == "scissor":
                print("ITS A TIE!")
                points_comp += 1
                points_user += 1
    print("YOUR POINTS IS :",points_user)
    print("COMPUTER`S POINT :",points_comp)
    if points_user == points_comp:
        print("IT'S A TIE!")
    elif points_user > points_comp:
        print("YOU WON!")
    else:
        print("YOU LOSE!")


print("WELCOME TO ROCK PAPER SCISSOR WITH COMPUTER\n")
print(
    "INSTRUCTION :\n YOU NEED TO SELECT BETWEEN ROCK PAPER SCISSORS\n AND YOU NEED TO SELECT THE NUMBERS FOR THAT .\n1.FOR ROCK\n2.FOR PAPER\n3.FOR SCISSORS ")
print("YOU NEED TO SPECIFY THE HOW MANY TIMES THE GAME SHOULD LAST\nIF YOU WIN THE POINTS ARE REWARDED \nTHE PLAYER WITH MAXIMUM POINT WINS THE GAME \n")
print("ENJOY PLAYING THE GAME")
turns = int(input("How many times should game need to last? "))
"""IT TAKES HOW MANY TIMES THE SHOULD BE PLAYED VAL -> INT CREATED BY SHASHWATH M"""
game()
while True:
    print("DO YOU WANT TO PLAY THE GAME AGAIN:")
    print("1.YES\t2.NO")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        game()
    elif choice == 2:
        break
print("GAME OVER")
print("THANKS FOR PLAYING")

