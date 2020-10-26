# Find all prime #s up to n
# 1 list all #s up to (starting from)
# identify first # in the list
# eliminate all multiples of that #
# repeat 2 and 3 until clone (sqrt n)
# have a boolean list or numbers

import math


def Main():
    # create an empty list
    isValid = []

    # ask user for the number
    num = int(input("Enter a number: "))

    # set the list value to True
    for i in range(num + 1):
        isValid.append(True)

    # iterating it up to the square root value of num
    # check if that index spot is True and find all the multiples of that and set it to false
    for j in range(2, int(math.sqrt(num)) + 1):
        if isValid[j]:
            multiple = j * j
            while multiple <= num:
                isValid[multiple] = False
                multiple = multiple + j

    # prints out the prime number if isValid is True
    length = len(isValid)
    count = 2
    while length > 2:
        if isValid[count]:
            print(count, end=" ")
        count = count + 1
        length = length - 1


Main()
