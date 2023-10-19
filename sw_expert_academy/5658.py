# 보물상자 비밀번호
import sys

read = sys.stdin.readline

T = int(read())

alpha_num = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

for t in range(T):
    N, K = map(int, read().split())
    cnt = N // 4
    words = read().rstrip()
    # dq = deque(read().rstrip())

    nums = []
    for i in range(cnt):
        if i == 0:
            pass
        else:
            words = words[-1] + words[:-1]

        nums.append(words[0:cnt])
        nums.append(words[cnt:cnt*2])
        nums.append(words[cnt*2:cnt*3])
        nums.append(words[cnt*3:N])

    nums = set(nums)
    results = []
    total = 0
    for num in nums:
        for c in range(cnt):
            total += 16 ** (cnt - c - 1) * alpha_num[num[c]]
        results.append(total)
        total = 0

    results = sorted(results, reverse=True)
    print(f'#{t+1} {results[K - 1]}')



