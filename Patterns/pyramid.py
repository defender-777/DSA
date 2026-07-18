# Half Pyramid:
n = 5

for i in range(1,n + 1):
    for j in range(i):
        print("*", end = " ")
    
    print()

# Full Pyramid 
n = 5

for i in range(1, n + 1):
    for j in range(n-i+1):
        print("*", end = " ")

    print()

# Right Half Pyramid

n = 5

for i in range(n):

    for j in range(n - i):
        print(" ", end = " ")

    for j in range(i):
        print("*", end = " ")

    print()

# Full Pyramid:
n = 5

for i in range(n):

    for j in range(n - i):
        print(" ", end = " ")

    for j in range(2*i-1):
        print("*", end = " ")

    print()


