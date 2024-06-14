
int_input = int(input())
width = 3 * int_input

for i in range(1,int_input+1):
    print (("H" * (2 * i - 1)).center(2*int_input -1,' '))
sp_wd= (2 * int_input -1)// 4 
for i in range(int_input +1):
    print( (" " * sp_wd )+("H" * int_input) + (" " * width)+ ("H" * int_input))
    
for i in range(int_input//2 + 1):
        print( (" " * sp_wd )+("H" * int_input * 5) )

for i in range(int_input +1):
    print( (" " * sp_wd )+("H" * int_input) + (" " * width)+ ("H" * int_input))
    
for i in range(int_input, 0, -1):
    pyramid_line = ("H" * (2 * i - 1)).center(2 * int_input - 1, ' ')
    print((" " * int_input* 4)+pyramid_line)    
