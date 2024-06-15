import numpy
num1, num2 = map(int, input().split())
arr = []
for _ in range(num1):
    arr.append(list(map(int, input().split())))
my_array = numpy.array(arr)
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
std_dev = numpy.std(my_array)
if std_dev == 0.0:
    print('0.0')
else:
    print(f"{std_dev:.11f}")
