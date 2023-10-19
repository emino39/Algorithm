def backtracking(cnt, total):
    global max_num, min_num

    if cnt == N:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total

    if ops[0]:
        ops[0] -= 1
        backtracking(cnt+1, total+numbers[cnt])
        ops[0] += 1
    if ops[1]:
        ops[1] -= 1
        backtracking(cnt+1, total-numbers[cnt])
        ops[1] += 1
    if ops[2]:
        ops[2] -= 1
        backtracking(cnt+1, total*numbers[cnt])
        ops[2] += 1
    if ops[3]:
        ops[3] -= 1
        backtracking(cnt+1, int(total/numbers[cnt]))
        ops[3] += 1

N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_num = int(-1e9)
min_num = int(1e9)

backtracking(1, numbers[0])

print(max_num, min_num, sep='\n')