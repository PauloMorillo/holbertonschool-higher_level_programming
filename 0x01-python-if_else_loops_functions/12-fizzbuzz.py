#!/usr/bin/python3
def fizzbuzz():
    count = 1
    while count <= 100:
        if ((count % 3) == 0) and ((count % 5) == 0):
            print("{} ".format("FizzBuzz"), end="")
            count = count + 1
        if (count % 3) == 0:
            print("{} ".format("Fizz"), end="")
#            count = count + 1
        elif (count % 5) == 0:
            print("{} ".format("Buzz"), end="")
#            count = count + 1
        else:
            print("{:d} ".format(count), end="")
        count = count + 1
