# Numbers 
n = 5
count = 1

for i in range(1,n+1):
    for j in range(i):
        print(count, end = " ")
        count += 1
    
    print()

#Alphabets

n = 5
count = ord('A')

for i in range(1,n+1):
    for j in range(i):
        print(chr(count), end = " ")
        count += 1
    
    print()