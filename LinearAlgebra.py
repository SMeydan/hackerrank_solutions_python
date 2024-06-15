import numpy
num = int(input())
arr = []
for _ in range(num):
    arr.append(list(map(float, input().split())))
print(round(numpy.linalg.det(numpy.array(arr)), 2))
