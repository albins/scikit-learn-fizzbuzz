#!/usr/bin/env python3

# "Write a program that prints the numbers from 1 to 100. But for
# multiples of three print “Fizz” instead of the number and for the
# multiples of five print “Buzz”. For numbers which are multiples of
# both three and five print “FizzBuzz”."

import sys


def fizzbuzz(n: int):
    mod3 = (n % 3) == 0
    mod5 = (n % 5) == 0

    if mod3 and mod5:
        return "FizzBuzz"
    elif mod5:
        return "Buzz"
    elif mod3:
        return "Fizz"
    else:
        return n


if __name__ == '__main__':

    for n in range(1, int(sys.argv[1])):
        print(fizzbuzz(n))
