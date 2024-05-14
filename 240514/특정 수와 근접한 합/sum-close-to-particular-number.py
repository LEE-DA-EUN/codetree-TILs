N, S = map(int, input().split())
ls = list(map(int, input().split()))
target = sum(ls)
ans = []
for i in range(len(ls)-1):
    for j in range(i+1, len(ls)):
        num = abs(target - ls[i] - ls[j]-S)
        ans.append(num)
print(min(ans))