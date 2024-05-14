ls = list(input())
s = 0
ans = 0
for i in range(len(ls)):
    if ls[i] == '(':
        s += 1
    elif ls[i] == ')':
        ans += s
print(ans)