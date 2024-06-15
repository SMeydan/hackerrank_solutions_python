import numpy
num1, num2 = map(int, input().split())
listed = []
for _ in range(num1):
    listed.append(list(map(int, input().split())))
np_array = numpy.array(listed)
print(numpy.max(numpy.min(np_array, axis=1)))
