import heapq

def solve(arr, k):
    if k > len(arr) or k <= 0:
        print("Invalid input")
        return
    
    heap = []
    result = []

    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    result.append(-heap[0][0])

    for i in range(k, len(arr)):
        heapq.heappush(heap, (-arr[i], i))
        
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        result.append(-heap[0][0])

    print(*result)

arr = list(map(int, input().split()))
k = int(input())
solve(arr, k)
