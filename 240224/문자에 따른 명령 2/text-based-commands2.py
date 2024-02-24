dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#L = 반시계 / R = 시계 / F = 이동
x = y = 0
num = 3
ls = list(input())
if 'F' not in ls:
    print(0, 0)
else:
    for i in range(len(ls)):
        if ls[i] == 'R':
            num = (num+1)%4
        elif ls[i] == 'L':
            num = (num+3)%4
        elif ls[i] == 'F':
            x += dx[num]
            y += dy[num]
    print(x, y)