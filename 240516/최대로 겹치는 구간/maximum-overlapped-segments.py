n = int(input())
ans = [0] * 201
for _ in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100 #offset
    x2 += (100-1) #시작점만 check
    for i in range(x1, x2+1):
        ans[i] += 1
print(max(ans))