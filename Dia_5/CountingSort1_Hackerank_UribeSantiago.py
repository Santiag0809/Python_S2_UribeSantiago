def countingSort1(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    return count

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(map(str, countingSort1(arr))))
