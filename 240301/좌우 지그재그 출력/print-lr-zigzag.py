n = int(input())
check = 1
for i  in range(1, n+1):
    ls = []
    for j in range(check, check+n):
        ls.append(j)
    check += n
    if i%2 == 0:
        ls.sort(reverse=True)
    print(*ls)