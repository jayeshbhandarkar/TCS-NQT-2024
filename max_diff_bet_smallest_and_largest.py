def solve(arr):
    largest, maxDiff = float('-inf'), float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        largest = max(largest, num)
        maxDiff = max(maxDiff, largest - num)
    return maxDiff

arr = list(map(int, input().strip("[]").split(',')))
print(solve(arr))
