# Clean Optimized Solution 
def isPrime(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for i in range(start, end + 1):
    if isPrime(i):
        print(i, end = " ")
