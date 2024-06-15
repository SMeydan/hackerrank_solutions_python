import re

n = int(input())
for _ in range(0, n):
    line = input()
    line = re.sub(r'\ [\&]{2,2}\ ', ' and ', line)
    line = re.sub(r'\ [\|]{2,2}\ ', ' or ', line)
    line = re.sub(r'\ [\&]{2,2}\ ', ' and ', line)
    line = re.sub(r'\ [\|]{2,2}\ ', ' or ', line)
    print(line)
