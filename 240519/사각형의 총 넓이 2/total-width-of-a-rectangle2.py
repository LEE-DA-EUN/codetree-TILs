n = int(input())
ls = [[0] * 201 for _ in range(201)]
for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1+100, x2+100):
        for j in range(y1+100, y2+100):
            ls[i][j] = 1
ans = 0
for i in range(201):
    ans += ls[i].count(1)
print(ans)