#Brute Force solution
"""
def isprime(n):

    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True 

result = isprime(5)

if result:
    print("Prime")
else :
    print("not prime")
"""
#Dynamic Input 
"""
def isprime(n):

    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True 
number = int(input("Enter the number : "))
result = isprime(number)

if result:
    print("Prime")
else :
    print("not prime")
"""
#Optimized Solution:
"""
def isprime(n):

    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True 

number = int(input("Enter the number : "))
result = isprime(number)

if result:
    print("Prime")
else :
    print("not prime")
"""
#Fully Optimized Clean Code:
def isPrime(n):

    if n <= 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

num = int(input("Enter the number: "))

result = isPrime(num)

if result:
    print("Prime")
else:
    print("Not Prime")