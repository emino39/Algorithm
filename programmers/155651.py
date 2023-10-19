from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    
    # 입력받은 시간을 분단위 정수로 변경
    for book in book_time:
        book[0] = int(book[0][:2]) * 60 + int(book[0][3:5])
        book[1] = int(book[1][:2]) * 60 + int(book[1][3:5])
    
    # 시작 시간을 기준으로 정렬
    book_time = sorted(book_time, key=lambda x: x[0])

    heap = []
    # book_time 돌면서 종료시각 확인
    for start, end in book_time:
        if not heap:
            heappush(heap, end)
            continue
        
        if heap[0] <= start:
            heappop(heap)
        else:
            answer += 1
        
        heappush(heap, end+10)

    
    return answer

if __name__ == "__main__":
    book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
    answer = solution(book_time)
    print(answer)