def subarray_equal_to_target(arr, n, target):
    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += arr[j]
            if curSum == target:
                print(arr[i:j+1])

def solve(arr, n, target):
    sumMap = {}
    curSum = 0
    for i in range(n):
        curSum += arr[i]

        if curSum == target:
            print(arr[:i+1])

        if curSum - target in sumMap:
            startIndex = sumMap[curSum - target] + 1
            print(arr[startIndex : i+1])

        sumMap[curSum] = i

arr = list(map(int, input().split()))
N = len(arr)
target = int(input())
solve(arr, N, target)
