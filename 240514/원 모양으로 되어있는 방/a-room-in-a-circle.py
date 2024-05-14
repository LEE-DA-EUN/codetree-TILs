N = int(input())
ls = [int(input()) for _ in range(N)]
answer = []

for _ in range(N):
    num = 0
    ans = 0
    for n in range(N):
        ans += ls[n]*num
        num += 1
    answer.append(ans)
    ls.append(ls.pop(0))
print(min(answer))