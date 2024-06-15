import numpy
num = int(input())
a, b = [], []
for _ in range(num):
    a.append(list(map(int, input().split())))
    
for _ in range(num):
    b.append(list(map(int, input().split())))
numpy_a, numpy_b = numpy.array(a), numpy.array(b)
print(numpy.dot(numpy_a, numpy_b))
