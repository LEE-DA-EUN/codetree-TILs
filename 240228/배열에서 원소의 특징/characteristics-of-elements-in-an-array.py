ls = list(map(int,input().split()))
for i in range(len(ls)):
    if ls[i]%3==0:
        print(ls[i-1])
        break