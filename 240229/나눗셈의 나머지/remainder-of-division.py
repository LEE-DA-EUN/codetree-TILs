a,b = map(int, input().split())
ls = [0] * b
while a > 1:    
    ls[a%b] += 1
    a = a//b
ans = 0
for i in ls:
    ans += i**2
print(ans)