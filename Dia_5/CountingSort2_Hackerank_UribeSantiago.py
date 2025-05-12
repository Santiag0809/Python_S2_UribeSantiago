def countingSort2(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(100):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(map(str, countingSort2(arr))))
