ls = list(input())
if '0' not in ls:
    ls[len(ls)-1] = '0'
else:
    for i in range(len(ls)):
        if ls[i] == '0':
            ls[i] = '1'
            break
ans = ''.join(ls)
print(int(ans,2))