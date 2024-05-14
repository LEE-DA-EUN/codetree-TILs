ls = list(input())
n = len(ls)
ans = 0
for i in range(n-2):
    for j in range(i+2, n-1):
        if ls[i] == ls[i+1] and ls[i] == '(':
            if ls[j] == ls[j+1] and ls[j] == ')':
                ans += 1
print(ans)