# 이진탐색

if __name__  == '__main__':
	N = int(input())
	cards = list(map(int, input().split()))
	cards = sorted(cards, reverse=False)
	M = int(input())
	numbers = list(map(int, input().split()))
	
	results = ''
	for m in range(M):
		flag = 0
		# index 끝 값
		left = 0
		right = N - 1
		while left <= right:
			mid = (left + right) // 2
			if cards[mid] == numbers[m]:
				results += '1 '
				flag = 1
				break
			elif cards[mid] > numbers[m]:
				right = mid - 1
			else:
				left = mid + 1
		
		if not flag:
			results += '0 '
	
	print(results)
