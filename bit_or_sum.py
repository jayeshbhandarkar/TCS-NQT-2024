def subarrayBitwiseORs(arr):
    res = set()
    curr = set()
    for num in arr:
        
        curr = {num | x for x in curr} | {num}
        res |= curr
    return len(res)

arr = list(map(int, input().split()))
print(subarrayBitwiseORs(arr))
