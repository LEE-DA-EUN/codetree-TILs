N, H, T = map(int, input().split())
ls = list(map(int, input().split()))
ans = []
for i in range(N-T+1):
    num = 0
    for j in range(i, i+T):
        num += abs(ls[j]-H)
    ans.append(num)
print(min(ans))