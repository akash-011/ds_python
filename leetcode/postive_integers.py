"""
https://leetcode.com/problems/perfect-number/description/

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

"""

from math import sqrt


def check_perfect_number(num):
    postive_divisors = [1]
    print(int(sqrt(6)))
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            postive_divisors.append(i)
            postive_divisors.append(int(num/i))


    if sum(postive_divisors) == num:
        return True 
    else:
        return False


print(check_perfect_number(28))