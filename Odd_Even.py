
def analyzer(number):
    odd = [1, 3, 5, 7, 9]
    even = [0, 2, 4, 6, 8]

    if int(number) in odd:
        print('Its an odd number!')
    elif int(number) in even:
        print('Its an even number!')
    else:print('nothing')

number = input('Enter a number:  ')
analyzer(number)