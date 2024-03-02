n = int(input())
num = 0
for i in range(1,n+1):    
    if i%2!=0:
        for j in range(n):
            num += 1
            print(num, end=' ')
    else:
        for j in range(n):
            num += 2
            print(num, end=' ')
    print()