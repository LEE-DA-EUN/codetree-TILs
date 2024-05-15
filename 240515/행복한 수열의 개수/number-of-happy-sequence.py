def cnt(ls):
    ans = 0
    for check in ls:
        for i in range(n-m+1):
            if check[i:i+m].count(check[i]) == m:
                ans += 1
                break
    return ans

n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
ans = 0
ans += cnt(ls)
ans += cnt(zip(*ls))
print(ans)