#iterative approach 
def factorial(n):

    if n < 0:
        raise ValueError("Negaitve Number")
    
    fact = 1

    for i in range(2, n +1):
        fact = fact * i
    
    return fact 

num = int(input())
print(factorial(num))

#Recursive approach
def factorial(n):
    if n < 0:
        raise ValueError("Negative number")
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
num = int(input())
print(factorial(num))