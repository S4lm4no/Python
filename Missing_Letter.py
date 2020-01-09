import random

correct = ['apple','bald','cat','dog']
wrong = ['appl_','bal_','c_t','d_g']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
rn = random.choice(letters)

while True:
    rn = random.choice(letters)
    new = wrong[0].replace(wrong[0][4] , rn)
    print(new)
    if new in correct:
        break
print('Your final word is: ' + str(new))