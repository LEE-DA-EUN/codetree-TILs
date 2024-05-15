n = int(input())
num = 0
min_num = 0
max_num = 0
for i in range(n):
    x, d = map(str, input().split())
    if d == 'R':
        num += int(x)
    elif d == 'L':
        num -= int(x)
    min_num = min(num, min_num)
    max_num = max(num, max_num)

white = abs(max_num - num)
black = abs(num - min_num)

print(white, black)