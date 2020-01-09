list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

while True:
    for i in list:
        print(i)
        new = i
        if new <= 5:
            new_list.append(new)
            list.remove(new)
            print(new_list)
        else:False

    long = len(list)
    sum = int(long) - int(len(list))
    if len(new_list) == sum:
        print("That's It!!")
        False


