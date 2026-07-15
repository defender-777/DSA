# Iterative approach:
'''
def fibonacci(n):

    if n <= 0:
        return
    
    prev = 0
    curr = 1
    
    for i in range(n):
        print(prev, end = " ")
        prev, curr = curr, prev + curr

num = int(input("Enter the number : "))
fibonacci(num)
'''
#Find Nth Fibonacci Number (0 - based indexing )
'''
def fibonacci(n):

    if n <= 0:
        return -1
    
    prev = 0
    curr = 1
    
    for i in range(n - 1):
        prev, curr = curr, prev + curr
    
    return curr

num = int(input("Enter the number : "))
result = fibonacci(num)
print(result)
'''
#Find Nth Fibonacci Number (1 - based indexing )
'''
def fibonacci(n):

    if n <= 0:
        return -1
    
    if n == 1:
        return 0
    
    prev = 0
    curr = 1
    
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    return curr

num = int(input("Enter the number : "))
result = fibonacci(num)
print(result)
'''

# Recursive Approach 
'''
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n - 2)

num = int(input("Enter the number : "))
result = fib(num)
print(result)

#To print all values:
for i in range(n + 1):
    print(fib(i),end= " ")

'''
# Dynamic Programming (Memoization)
def fib(n , memo):
    if n <= 1:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n - 2, memo)
    return memo[n]
n = int(input())
memo = [-1] * (n + 1)
for i in range(n):
    print(fib(i,memo))


