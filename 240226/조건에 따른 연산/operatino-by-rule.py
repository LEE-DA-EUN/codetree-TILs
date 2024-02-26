num = int(input())
cnt = 0
while True:
    if num%2 == 0:
        num = num*3+1
    else:
        num = num*2+2
    cnt += 1
    if num >= 1000:
        print(cnt)
        break