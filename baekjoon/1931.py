N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
# 종료 시간 순으로 정렬
times = sorted(times, key=lambda x: (x[1], x[0]))

max_cnt = 0
end = 0
cnt = 0

for i in range(N):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]
    else:
        continue

if max_cnt <= cnt:
    max_cnt = cnt

print(max_cnt)