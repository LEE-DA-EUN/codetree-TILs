ls = []
for _ in range(2):
    a,b = map(str,input().split())
    if int(a) >= 19 and b == 'M':
        ans = 1
        break
    ans = 0
print(ans)