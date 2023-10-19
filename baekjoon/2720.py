N = int(input())

for n in range(N):
    money = int(input())
    coins = [0, 0, 0, 0]

    while True:
        if money == 0:
            break

        if money >= 25:
            coins[0] = (money // 25)
            money = (money % 25)
        elif money >= 10:
            coins[1] = (money // 10)
            money = (money % 10)
        elif money >= 5:
            coins[2] = (money // 5)
            money = (money % 5)
        else:
            coins[3] = (money // 1)
            money = (money % 1)

    for coin in coins:
        print(coin, end=' ')
    print()


"""
for n in range(N):
    money = int(input()) / 100
    coins = [0, 0, 0, 0]

    while True:
        if money == 0:
            break

        if money >= 0.25:
            coins[0] = round(money // 0.25)
            money = round(money % 0.25, 2)
        elif money >= 0.1:
            coins[1] = round(money // 0.1)
            money = round(money % 0.1, 2)
        elif money >= 0.05:
            coins[2] = round(money // 0.05)
            money = round(money % 0.05, 2)
        else:
            coins[3] = round(money // 0.01)
            money = round(money % 0.01, 2)

    for coin in coins:
        print(coin, end=' ')
    print()
"""
