price = int(input())
money = [500, 100, 50, 10, 5, 1]
rest = 1000 - price
cnt = 0 # 거스름돈 개수

for m in money:
    if rest == 0:
        break
    else:
        if rest >= m:
            tmp = rest // m
            cnt += tmp
            rest = rest % m
        else:
            pass

print(cnt)