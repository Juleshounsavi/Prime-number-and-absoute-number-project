#Prime number recognition project.
def is_prime(n):
    """
    This function will check if a natural number is a prime or not by returning True if it is and False if it's not. 
    A prime number is a natural number greater than 1 that possesses a special property: it can only be divided evenly by 1 and itself. 
    In simpler terms, it cannot be represented as the product of two or more smaller numbers, excluding 1.
    """
    if n<=1: 
        return False
    else:
        for i in range(2 , int(n/2)+1): 
            if n % i == 0:
                return False
        else:
            return True

