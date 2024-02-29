ls = []
ans = 0
for i in range(4):
    n = list(map(int, input().split()))
    ls.append(n)
for i in range(4):
    for j in range(i+1):
        ans += ls[i][j]
print(ans)