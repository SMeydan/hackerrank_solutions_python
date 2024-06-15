# Enter your code here. Read input from STDIN. Print output to STDOUT
size1 = int(input())
user_input1 = input()
size2 = int(input())
user_input2 = input()

lis1 = map(int,user_input1.split())
myset1 = set(lis1)

lis2 = map(int,user_input2.split())
myset2 = set(lis2)

result = myset2.symmetric_difference(myset1)
s_result = sorted(result)

for x in s_result:
    print(x)
