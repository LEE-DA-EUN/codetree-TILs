def makeList(num):
    ls = []
    for _ in range(num):
        ls.append(list(map(int, input().split())))
    return ls


n, m = map(int, input().split())
ls1 = makeList(n)
ls2 = makeList(n)

for i in range(n):
    for j in range(m):
        num = 0
        if ls1[i][j] != ls2[i][j]:
            num = 1
        print(num, end=' ')
    print()