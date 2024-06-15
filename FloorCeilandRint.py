import numpy
numpy.set_printoptions(legacy='1.13')
num_list = numpy.array(list(map(float, input().split())))
print(numpy.floor(num_list))
print(numpy.ceil(num_list))
print(numpy.rint(num_list))
