a = int(input())
ls = list(map(int, input().split()))
for i in range(4):
    print(1 if a>ls[i] else 0)