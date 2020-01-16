import pandas as pd

df = pd.read_csv('new_passwords.csv')

passwords = df.ALL

user = input('Enter your password: ')
for i in passwords:
    if i == user:
        print('===password cracked successfully===')
        print('Your password is: ' + str(i))
        break
    else:
        print('your password was not found!')

