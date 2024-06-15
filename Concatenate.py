import numpy
num1, num2, num3 = map(int, input().split())
arr1, arr2 = [], []
for i in range(num1 + num2):
    if i < num1:
        arr1.append(list(map(int, input().split())))
    else:
        arr2.append(list(map(int, input().split())))
print(numpy.concatenate((arr1, arr2), axis = 0))
