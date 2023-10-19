
N, M = map(int, input().split(' '))

n_dict = {}

for n in range(N):
	word = input()
	if word not in n_dict.keys():
		n_dict[word] = 1

cnt = 0

for m in range(M):
	new = input()
	if new in n_dict.keys():
		cnt += 1


print(cnt)
