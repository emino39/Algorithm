# '최솟값'이므로 '-' 연산자 기준으로 split
numbers = input().split('-')
print(numbers)

sum_list = []

for n in numbers:
    tmp_sum = 0
    tmp = n.split('+')

    for t in tmp:
        tmp_sum += int(t)
    
    sum_list.append(tmp_sum)

total = sum_list[0]

for s in sum_list[1:]:
    total -= s