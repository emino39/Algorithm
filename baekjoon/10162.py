T = int(input())
time = [300, 60, 10]
cnt = [0, 0, 0]

if T % 10 != 0:
    print(-1)
else:
    for idx, t in enumerate(time):
        cnt[idx] = T // t
        T = T % t

    print(' '.join(map(str, cnt)))