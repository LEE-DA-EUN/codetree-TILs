n = int(input())
ls = list(map(int, input().split()))
ans = []
for i in range(n):
    num = 0
    for j in range(n):
        num += ls[j] * abs(i-j)
    ans.append(num)
print(min(ans))