def solution(x, y, n):
    arr = [float('inf')] * (y+1)
    arr[x] = 0
    
    for i in range(x, y+1):
        # if arr[i] == float('inf'):
        #     continue
        
        if (i + n) <= y:
            arr[i + n] = min(arr[i + n], arr[i] + 1)
        
        if (i * 2) <= y:
            arr[i * 2] = min(arr[i * 2], arr[i] + 1)
        
        if (i * 3) <= y:
            arr[i * 3] = min(arr[i * 3], arr[i] + 1)
    
    if arr[y] == float('inf'):
        return -1
    else:
        return arr[y]

"""
def solution(x, y, n):
    arr = [0] * (y+1)
    
    for i in range(x, y+1):
        if (i - n) >= x:
            arr[i] = arr[i - n] + 1
        
        if (i % 2) == 0:
            arr[i] = min(arr[i], arr[i//2] + 1)
        
        if (i % 3) == 0:
            arr[i] = min(arr[i], arr[i//3] + 1)
    
    
    if arr[y] == 0:
        return -1
    else:
        return arr[y]
"""

if __name__ == "__main__":
    answer = solution(10, 40, 5)

    print(answer)