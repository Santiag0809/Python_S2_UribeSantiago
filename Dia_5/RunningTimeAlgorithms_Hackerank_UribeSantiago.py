def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = value
    return shifts

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(runningTime(arr))
