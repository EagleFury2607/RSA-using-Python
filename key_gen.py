import sympy
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def generate_key():
     #Step 1:
     p = sympy.randprime(50,100)
     q = sympy.randprime(1,50)

     #Step 2:
     n = p * q

     #Step 3:
     lambda_n = lcm(p-1, q-1)

     #Step 4:
     e = sympy.randprime(1,lambda_n-1)

     #Step 5:
     d = modInverse(e, lambda_n)
     return ((e, n), (d, n))
