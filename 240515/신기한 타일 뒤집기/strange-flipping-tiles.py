n = int(input())
num = 0
min_num = 0
max_num = 0
before = ''

for i in range(n):
    x, d = map(str, input().split())
    if d == 'R':
        if before == 'R':
            num -= 1
        num += int(x)
    elif d == 'L':
        if before == 'L':
            num += 1
        num -= int(x)
    min_num = min(num, min_num)
    max_num = max(num, max_num)
    before = d

white = abs(max_num - num)
black = abs(num - min_num)

print(white, black)