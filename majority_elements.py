def findMajorityElement(arr, N):
    freq = {}
    result = []
    for num in arr:
        if num in freq:
            freq[num] += 1 
        else:
            freq[num] = 1
    for key, val in freq.items():
        if val >= N // 3:
            result.append(key)
    return result

arr = list(map(int, input().strip("[]").split(','))) 
print(*findMajorityElement(arr, len(arr)))
