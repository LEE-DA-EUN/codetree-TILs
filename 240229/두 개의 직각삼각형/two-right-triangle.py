n = int(input())
for i in range(n, 0, -1):
    j = (n-i)*2
    ans = '*' * i + ' ' * j + '*' * i
    print(ans)