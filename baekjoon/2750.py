
def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len-1, 0, -1):
        for j in range(i):
            tmp = 0
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    return arr

def python_sort(arr):

    return sorted(arr, reverse=False)

if __name__ == '__main__':
    N = int(input())

    numbers = []

    for n in range(N):
        numbers.append(int(input()))

    # numbers = bubble_sort(numbers)
    numbers = python_sort(numbers)

    for k in numbers:
        print(k)