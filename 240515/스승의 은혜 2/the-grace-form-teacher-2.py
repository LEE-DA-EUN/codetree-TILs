N, B = map(int, input().split())
ls = [int(input()) for _ in range(N)]
num = 0
ls.sort()
for i in range(N):
    num += ls[i]
    if num > B:
        if num-ls[i]/2 <= B:
            print(i+1)
        else:
            print(i)
        break