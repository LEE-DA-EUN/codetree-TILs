ls = []
while True:
    num = int(input())
    if num > 29 or num < 20:
        break
    else:
        ls.append(num)
ans = sum(ls)/len(ls)

print(f"{ans:.2f}")