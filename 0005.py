"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

current_number = 20
max_successful = 1
found = 0

# TODO Performance here is awful

while found == 0:
    current_number += 1

    for test_num in range(1,21):
        if current_number % test_num == 0:
            if test_num > max_successful: 
                max_successful = test_num
                print(f"New winner: {current_number} is divisible by all to {max_successful}")
            
            if test_num == 20 and current_number % test_num == 0:
                found = 1
                print(f"{current_number} divisible by 1..20")
                break
        else:
            break