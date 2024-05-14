R, C = map(int, input().split())
ls = []
ans = 0
for _ in range(R):
    ls.append(list(map(str, input().split())))

for i in range(1, R):
    for j in range(1, C):
        for x in range(i+1, R-1):
            for y in range(j+1, C-1):
                if ls[0][0] != ls[i][j] and ls[i][j] != ls[x][y] and ls[x][y]!= ls[R-1][C-1]:
                    ans += 1
print(ans)