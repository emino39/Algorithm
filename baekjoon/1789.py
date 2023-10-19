# 서로 다른 N개의 자연수의 합이 S, N의 최댓값
# => 1부터 더하면 됨

S = int(input())

total = 0
N = 0
c = 1
while True:
    if total > S:
        N -= 1
        break
    else:
        total += c
        N += 1
        c += 1

print(N)


