import random

print("Enter the following details to create a password....")
number = int(input("Enter the amount of number to be added in password: "))
"""number is used to recieve input from the user to create the total amount of value in password : created by Shashwath M"""

letters = int(input("Enter the amount of letters to be added in password: "))
"""number is used to recive input from the user to create the total amount of value in password " created by Shashwath M"""

special = input("Enter the special characters to be added in password: ")
"""it recieves the special character as input as shows it in result : created by Shashwath M"""

password = []
"""List to show password"""

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(number - 1):
    x = random.randint(0, 9)
    password.append(x)

for i in range(letters):
    x = random.choice(characters)
    password.append(x)

for i in special:
    password.append(i)

random.shuffle(password)
string = "".join(map(str, password))
print(string)