n = int(input())
ans = 0
for i in range(1,n+1):
    n = n//i
    ans += 1
    if n <= 1:
        print(ans)
        break