# Enter your code here. Read input from STDIN. Print output to STDOUT
num_a = int(input())
a = set(map(int, input().split()))
num_s = int(input())
for i in range(num_s):
    inst = input().split()
    s = set(map(int, input().split()))
    
    if inst[0] == "update":
        a.update(s)
    elif inst[0] == "intersection_update":
        a.intersection_update(s)
    elif inst[0] == "difference_update":
        a.difference_update(s)
    elif inst[0] == "symmetric_difference_update":
        a.symmetric_difference_update(s)

print(sum(a))
