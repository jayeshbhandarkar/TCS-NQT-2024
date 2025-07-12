def isPrime(number):
    if number <= 1: 
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def calculateSum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10 
    return isPrime(total)

n, m = map(int, input().split())

for i in range(n, m + 1):
    if isPrime(i) and calculateSum(i):
        print(i)
