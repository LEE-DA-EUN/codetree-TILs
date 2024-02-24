dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#L = 반시계 / R = 시계 / F = 이동
x = y = 0
num = 3
ls = list(input())
for i in range(len(ls)):
    if ls[i] == 'R':
        num = (num+1)%4
        x, y = dx[num], dy[num]
    elif ls[i] == 'L':
        num = (num+3)%4
        x, y = dx[num], dy[num]
    elif ls[i] == 'F':
        print(x, y)