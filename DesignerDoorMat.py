# Enter your code here. Read input from STDIN. Print output to STDOUT
user_input = input()
sp_list = user_input.split(' ')
width,height =  int(sp_list[1]), int(sp_list[0])
for i in range(1,height//2+1):
    print(((2*i -1) * ".|.").center(width, '-'))
print(("WELCOME").center(width, '-'))
for i in range(height//2,0,-1):
    print(((2*i -1) * ".|.").center(width, '-'))
