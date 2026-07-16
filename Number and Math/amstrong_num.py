def amstrong(n):

    if n <= 1:
        return False
    original = n
    count = len(str(n))

    total = 0

    while ( n !=0 ):
        digit = n % 10
        total = total + digit ** count
        n = n // 10

    return total == original

num = int(input())
print(amstrong(num))