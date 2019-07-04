from math import sqrt, ceil

def is_prime(n):
    """
    Returns True if the number provided is prime
    """
    
    # Some basic rules
    if n <= 1: return False
    # 2 is a prime number
    if n == 2: return True

    # Highest number to check is square root of the input number
    max_check = ceil(sqrt(n))
    
    # Otherwise, if it's divisible by 2, not a prime
    if n % 2 == 0: return False

    # TODO is max_check + 1 required? 
    for num in range(3, max_check+1, 2):
        if n % num == 0: return False
    
    # Number passes primality test
    return True

def prime_factors(n):
    """
    Returns a list of prime factors for a given number
    """

    factors = []

    # append 2 so long as n is divisible by it
    while n % 2 == 0: 
        factors.append(2)
        n = n / 2
          
    # continue to find factors
    for i in range(3,int(sqrt(n))+1,2): 
        # while n is divisible by i, append and continue to next
        while n % i== 0: 
            factors.append(i)
            n = n / i
    
    return factors