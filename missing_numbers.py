def getMissingNumber(arr, size):
    totalSum = sum(arr)
    n = size + 1
    actualSum = (n * (n + 1)) // 2
    return actualSum - totalSum

N = int(input())
arr = list(map(int, input().split(',')))
print(getMissingNumber(arr, N))
