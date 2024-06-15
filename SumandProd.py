import numpy
num1, num2 = map(int, input().split())
arr = []
for i in range(num1):
    arr.append(list(map(int, input().split())))
np_array = numpy.array(arr)
print(numpy.prod(numpy.sum(np_array, axis=0)))

