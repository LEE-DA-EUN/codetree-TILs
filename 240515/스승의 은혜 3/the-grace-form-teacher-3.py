N, B = map(int, input().split())
P = []
S = []
ans = 0
for i in range(N):
    p, s = map(int, input().split())
    P.append(p)
    S.append(s)

for i in range(N):
    num = 0
    P[i] /= 2 #쿠폰 사용

    ls = [(P[x] + S[x]) for x in range(N)]
    ls.sort()

    for j in range(N):
        num += ls[j]
        if num > B:
            ans = max(ans, j)
            break

    P[i] *= 2 #쿠폰 사용한 것 복구
    

print(ans)