import math_lib as math_lib

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest_palindrome = 0

# HACK this looks pretty ugly
for x in range(100,1000):
    for y in range(100,1000):
        if math_lib.is_palindrome(x*y):
            if x*y > largest_palindrome:
                largest_palindrome = x*y

print(largest_palindrome)