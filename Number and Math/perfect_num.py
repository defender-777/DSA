def perfect(n):

    if n <= 1:
        return False
    
    divisor_sum = 0

    for i in range(1,n):
        if n % i == 0:
            divisor_sum = divisor_sum + i
        
    return divisor_sum == n

num = int(input())
print(perfect(num))