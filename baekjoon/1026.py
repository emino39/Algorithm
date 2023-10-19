N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0

for n in range(N):
    a_idx = a.index(min(a))
    b_idx = b.index(max(b))

    a_min = a.pop(a_idx)
    b_max = b.pop(b_idx)

    total += (a_min * b_max)

print(total)