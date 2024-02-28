num = int(input())
ls = list(map(int, input().split()))
for i in range(num-1, -1,-1):
    if ls[i]%2==0:
        print(ls[i], end=' ')