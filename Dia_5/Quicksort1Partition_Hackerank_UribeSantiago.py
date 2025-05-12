def quickSort(arr):
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    return left + equal + right

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(map(str, quickSort(arr))))
