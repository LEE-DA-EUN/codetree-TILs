ls = list(map(str, input().split('-')))
ls[1], ls[2] = ls[2], ls[1]
ans = '-'.join(ls)
print(ans)