"""
It is common practice, in Python, to
use 'args' in flexible argument parameter
"""


def addition(*args):
    total_sum = 0
    for a in args:
        total_sum += a
    print(total_sum)


"""
However, you can use any word to be
used in flexible argument parameter
"""


def subtraction(*number):
    total_difference = 0
    for a in number:
        total_difference -= a
    print(total_difference)


addition(2)
addition(9, 32)
addition(42, 7, 11)
subtraction(78)
subtraction(99, 88, 65)
subtraction(9, 12, 28, 99)
