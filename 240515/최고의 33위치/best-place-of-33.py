N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-2):
    num = 0
    for j in range(N-2):
        num = ls[i][j] + ls[i][j+1] + ls[i][j+2] + ls[i+1][j] + ls[i+1][j+1] + ls[i+1][j+2] + ls[i+2][j] + ls[i+2][j+1] + ls[i+2][j+2]
        ans = max(ans, num)
print(ans)