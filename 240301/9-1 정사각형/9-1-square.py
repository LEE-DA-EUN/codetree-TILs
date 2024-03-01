n = int(input())
num = 10
for i in range(n):
    for j in range(n):
        num -= 1
        if num == 0:
            num = 9
        print(num, end='')
    print()