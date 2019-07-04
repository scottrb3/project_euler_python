import math_lib as math_lib

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143

prime_factors = []

for i in range(num):
    if math_lib.is_prime(i) == True:
        prime_factors.append(i)
        print(i)

print(prime_factors)