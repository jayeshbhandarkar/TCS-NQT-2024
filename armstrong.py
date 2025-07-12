def isArmStrongNumber(n, k):
    total = 0
    originalNum = n
    while originalNum > 0:
        digit = originalNum % 10 
        total += digit ** k 
        originalNum //= 10  
    return total == n

def main():
    arr = input().strip('[]').split(',')
    flag = False

    for num_str in arr:
        num = int(num_str.strip())
        k = len(str(num))
        if isArmStrongNumber(num, k):
            print(num, end=" ")
            flag = True

    if not flag:
        print("No Armstrong numbers present")

main()
