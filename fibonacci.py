def fibonacci(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    
    prev2, prev = 0, 1
    fibSum = 1

    for i in range(2, n):
        cur = prev2 + prev 
        fibSum += cur
        prev2, prev = prev, cur
        
    return fibSum

n = int(input())
print(fibonacci(n))
