def distance(x1,y1,x2,y2):
    num = abs(x1-x2) + abs(y1-y2)
    return num

N = int(input())
ls = []
ans = []
for _ in range(N):
    ls.append(list(map(int, input().split())))

for i in range(1, N-1): #건너뛰는 체크포인트
    d = 0
    idx = 0
    for j in range(1, N):
        if i == j: #체크포인트 건너뛰기
            continue
        d += distance(ls[idx][0], ls[idx][1], ls[j][0], ls[j][1])
        idx = j
    ans.append(d)

print(min(ans))