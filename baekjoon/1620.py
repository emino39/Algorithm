import sys

N, M = map(int, input().split())

word_dict = {}
num_dict = {}

for n in range(N):
	t = sys.stdin.readline().strip()
	word_dict[n+1] = t
	num_dict[t] = n+1

for m in range(M):
	i = sys.stdin.readline().strip()
	if i.isdigit():
		print(word_dict[int(i)])
	else:
		print(num_dict[i])
