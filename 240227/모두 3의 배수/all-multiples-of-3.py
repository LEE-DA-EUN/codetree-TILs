ans = 1
for _ in range(5):
    i = int(input())
    if i%3!=0:
        ans = 0
        break
print(ans)