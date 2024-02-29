n = int(input())
ls = list(map(int, input().split()))
check = []
for i in range(len(ls)-1):
    check.append(ls[i+1]- ls[i])

print(min(check))