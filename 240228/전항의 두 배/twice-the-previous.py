ls = [0] * 10
ls[0], ls[1] = map(int, input().split())

for i in range(2, 10):
    ls[i] = ls[i-1] + ls[i-2]*2

for i in range(10):
    print(ls[i], end=' ')