n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
ans = -1

def check(x1,x2,y1,y2): #양수만 있는지 확인
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if ls[i][j] <= 0:
                return False
    return True


for i in range(n):
    for j in range(m):
        for x in range(i, n):
            for y in range(j, m):
                if check(i,x,j,y):
                    num = (x-i+1)*(y-j+1)
                    ans = max(ans, num)
print(ans)