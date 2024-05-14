n = int(input())
ls = list(map(int, input().split()))
ans = 0
for i in range(n-2):
    for j in range(i+2, n):
        num = ls[i]+ls[j]
        ans = max(ans, num)
print(ans)