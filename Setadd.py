# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
s = set('')
for i in range(size):
    s.add(input())
    
print(len(s))
