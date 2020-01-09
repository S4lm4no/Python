import random as rn

def pass_generator(length1):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    password = ''


    length = length1

    while int(length1) > 0:
        let = rn.choice(letters)
        num = rn.choice(numbers)
        sym = rn.choice(symbols)

        password = password + let
        password = password + num
        password = password + sym
        length1 = int(length1) - 1

    cut = int(length) + 1

    # print the password
    print(password[0:int(length)])

length1 = input('Enter the length of your password:  ')
pass_generator(length1)
