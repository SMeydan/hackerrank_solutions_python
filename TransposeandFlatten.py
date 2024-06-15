import numpy
rows, columns = map(int, input().split())
listed = []
for row in range(rows):
    listed.append(list(map(int, input().split())))
numpy_array = numpy.array(listed)
print(numpy.transpose(numpy_array))
print(numpy_array.flatten())

