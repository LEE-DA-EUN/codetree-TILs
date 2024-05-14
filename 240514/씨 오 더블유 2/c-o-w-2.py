N = int(input())
ls = list(input())
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if ls[i] == 'C' and ls[j]=='O' and ls[k] == 'W':
                ans += 1
print(ans)