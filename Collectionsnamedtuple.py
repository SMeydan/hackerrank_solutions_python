from collections import namedtuple
number, Student, total = int(input()), namedtuple('Student', input()), 0
[total := total + int(Student(*input().split()).MARKS) for _ in range(number)]
print(total/number)
    
