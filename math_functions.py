
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

##############################################################################

def is_prime(n):
    if type(n) != int or n <= 0 :
        raise TypeError("is_prime: Invalid input")
    elif n == 1:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
##############################################################################

def phi(n):
    res = n
    if type(n) != int or n <= 0 :
        raise TypeError("phi: Invalid input")
    elif is_prime(n) == True:
        return n-1
    else:
        for p in range(1,n+1):
            if is_prime(p) == True and n%p ==0:
                res *= 1-1/p
    return int(round(res , 0))

##############################################################################

def is_semi_prime(n):
    if type(n) != int or n <= 0 :
        raise TypeError("is_semiprime: Invalid input")
    elif is_prime(n) == True or n==1:
        return False
    else:
        i = 2
        # number of prime divisors
        count = 0
        while i < n and count <= 2:
            if n%i == 0:
                if is_prime(i) == False:
                    return False
                else:
                    count += 1
            i += 1
    if count == 2:
        return True
    else:
        return False
    
##############################################################################

def are_comprime(m , n):
    from math import gcd
    if type(m) != int or m <= 0 :
        raise TypeError("are_comprime: First argument invalid")
    if type(n) != int or n <= 0 :
        raise TypeError("are_comprime: Second argument invalid")
    if gcd(m,n) == 1:
        return True
    else:
        return False

##############################################################################

def prime_finder(size):
    try:
        from numpy.random import randint 
    except:
        print("NumPy not found, proceeding with math library...")
        from random import randrange as randint
    from numpy.random import randint 
    p = randint(2**(size-1),2**size + 1)
    if is_prime(p) == True:
        del randint
        return p
    else:
        del randint
        return prime_finder(size)

##############################################################################
   
