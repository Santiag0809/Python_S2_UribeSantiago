def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(' '.join(map(str, arr)))
        i -= 1
    arr[i + 1] = value
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    insertionSort1(n, arr)
