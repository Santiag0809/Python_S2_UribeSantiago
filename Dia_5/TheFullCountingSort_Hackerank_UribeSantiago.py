def countSort(arr):
    result = [[] for _ in range(100)]
    for i in range(len(arr)):
        num, string = int(arr[i][0]), arr[i][1]
        if i < len(arr) // 2:
            result[num].append('-')
        else:
            result[num].append(string)
    print(' '.join([s for group in result for s in group]))

if __name__ == '__main__':
    n = int(input())
    arr = [input().split() for _ in range(n)]
    countSort(arr)
