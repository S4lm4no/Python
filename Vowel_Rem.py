
word = input('Enter a word:  ')
i = 15
while i > 0:
    if 'a' in word:
        word = word.replace('a', '')
        i = int(i) - 1
        continue


    elif 'e' in word:
        word = word.replace('e', '')
        i = int(i) - 1
        continue



    elif 'i' in word:
        word = word.replace('i', '')
        i = int(i) - 1
        continue



    elif 'o' in word:
        word = word.replace('o', '')
        i = int(i) - 1
        continue


    elif 'u' in word:
        word = word.replace('u', '')
        i = int(i) - 1
        continue


    else:print('----------Done!----------')
    print(word)
    break





