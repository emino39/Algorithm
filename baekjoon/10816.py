import sys

N = sys.stdin.readline()
nums = map(int, sys.stdin.readline().split())
M = sys.stdin.readline()
find_nums = map(int, sys.stdin.readline().split())

num_dict = {}

for n in nums:
	if n in num_dict:
		num_dict[n] += 1
	else:
		num_dict[n] = 1

# results = ''

print(' '.join(str(num_dict[m]) if m in num_dict else '0' for m in find_nums))

"""
for m in find_nums:
	if m in num_dict:
		results.join(str(num_dict[m]))
	else:
		results.join('0')

print(results)
"""
