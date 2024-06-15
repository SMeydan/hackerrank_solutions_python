# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())
for i in range(test_cases):
    a_num = int(input())
    a = input().split()
    b_num = int(input())
    b = input().split()
    
    if set(a).issubset(set(b)):
        print(True)
    else:
        print(False)
