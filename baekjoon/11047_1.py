N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = sorted(coins, reverse=True)

total = 0

while K > 0:
    for coin in coins:
        if K == 0:
            break
        
        if coin > K:
            continue
        
        total += (K // coin)
        K = K % coin
        
print(total)