# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split()
num_of_sets = int(input())
is_all = True
for i in range(num_of_sets):
    sets = input().split()
    if not set(sets).issubset(a):
        is_all = False
        
print(is_all)

