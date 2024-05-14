n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(n-2):
        num = ls[i][j] + ls[i][j+1] + ls[i][j+2]
        ans = max(ans, num)
print(ans)