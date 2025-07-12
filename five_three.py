def solve(arr, N):
    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            print("ThreeFive", end = " ")
        elif num % 5 == 0:
            print("Five", end = " ")
        elif num % 3 == 0:
            print("Three", end = " ")
        else:
            print(num, end = " ")

N = int(input())
arr = list(map(int, input().strip('[]').split(',')))
solve(arr, N)
