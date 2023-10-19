from itertools import permutations

def cal(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        if a < 0:
            tmp = a * (-1) // b
            return tmp * (-1)
        else:
            return a // b


N = int(input())
numbers = list(map(int, input().split()))
ops_cnt = list(map(int, input().split()))

max_result = -1000000000
min_result = 1000000000
ops = []

for i in range(4):
    for j in range(ops_cnt[i]):
        if i == 0:
            ops.append('+')
        elif i == 1:
            ops.append('-')
        elif i == 2:
            ops.append('*')
        else:
            ops.append('//')

for perm in permutations(ops):
    res = numbers[0]
    for n in range(1, N):
        res = cal(res, numbers[n], perm[n-1])

    if max_result < res:
        max_result = res
    if min_result > res:
        min_result = res

print(max_result)
print(min_result)