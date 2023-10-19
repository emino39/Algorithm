

if __name__ == '__main__':
	N, k = map(int, input().split())
	scores = list(map(int, input().split()))

	scores = sorted(scores, reverse=True)
	print(scores[k-1])

