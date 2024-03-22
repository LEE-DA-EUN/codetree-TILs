ans = []
ls = list(input())
for i in range(1,len(ls),2):
    ans.append(ls[i])
ans.reverse()
print(''.join(ans))