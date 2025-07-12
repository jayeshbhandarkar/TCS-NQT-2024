def findCubeSum(start, end):
    cubeSum = 0
    for i in range(start, end+1):
        cubeSum += i ** 3 
    print(cubeSum)

start, end  = map(int, input().split())
findCubeSum(start, end)
