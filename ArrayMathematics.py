import numpy
num1, num2 = map(int, input().split())
a, b = [], []
for i in range(num1):
    a.append(list(map(int, input().split())))
for i in range(num1):
    b.append(list(map(int, input().split())))

numpy_a = numpy.array(a, float)
numpy_b = numpy.array(b, float)

print(numpy.add(numpy_a, numpy_b).astype(int))
print(numpy.subtract(numpy_a, numpy_b).astype(int))
print(numpy.multiply(numpy_a, numpy_b).astype(int))
print(numpy.floor_divide(numpy_a, numpy_b).astype(int))
print(numpy.mod(numpy_a, numpy_b).astype(int))
print(numpy.power(numpy_a, numpy_b).astype(int))
