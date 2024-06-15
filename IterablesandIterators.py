from math import factorial

size = int(input())
arr = input().split()
repeat = int(input())

counter = arr.count('a')

combination = factorial(size)/(factorial(repeat)*factorial(size - repeat))
if size != repeat:    
    without_a_combination = factorial(size - counter)/(factorial(repeat)*factorial(size - counter - repeat))
else:
    without_a_combination = 1 if counter == 0 else 0
print("%.12f" % ((combination - without_a_combination) / combination))
