import numpy
numpy.set_printoptions(legacy='1.13')
num1, num2 = map(int, input().split())
print(numpy.eye(num1, num2, k=0))

