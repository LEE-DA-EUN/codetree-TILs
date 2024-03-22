ans = []
for i in range(3):
    ls = list(input())
    ans.append(len(ls))
print(max(ans) - min(ans))