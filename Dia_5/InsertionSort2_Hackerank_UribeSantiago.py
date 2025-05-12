def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    insertionSort2(n, arr)
