N, K = map(int, input().split())
ans = [0] * (N+1)
for _ in range(K):
    A, B = map(int, input().split())
    for i in range(A,B+1):
        ans[i] += 1
print(max(ans))