n = int(input())
ls = list(map(int, input().split()))
ans = []
for i in range(len(ls)):
    ans.append(ls[i])
    if len(ans)%2==0:
        continue
    else:
        ans.sort()
        mid = len(ans)//2
        print(ans[mid], end=' ')