# Enter your code here. Read input from STDIN. Print output to STDOUT
num, res = map(int, input().split())
polynomial = input().split()
result = 0
if num == 0:
    res = 0
else:
    for i in range(len(polynomial)):
        if i% 2 == 0 and i== 0:
            if polynomial[i].startswith('x'):
                if len(polynomial[i]) == 1:
                    result += num
                else:
                    result += pow(num, int(polynomial[i][-1]))
            else:
                if len(polynomial[i]) == 1:
                    result += int(polynomial[i])
                else:
                    co_x, power = polynomial[i].split('**')
                    co, x = co_x.split('*')
                    result += int(co) * pow(num, int(power))
        elif i% 2 == 0 and polynomial[i-1] == '+':
            if polynomial[i].startswith('x'):
                if len(polynomial[i]) == 1:
                    result += num
                else:
                    result += pow(num, int(polynomial[i][-1]))
            else:
                if len(polynomial[i]) == 1:
                    result += int(polynomial[i])
                else:
                    co_x, power = polynomial[i].split('**')
                    co, x = co_x.split('*')
                    result += int(co) * pow(num, int(power))
        elif i% 2 == 0 and polynomial[i-1] == '-':
            if polynomial[i].startswith('x'):
                if len(polynomial[i]) == 1:
                    result -= num
                else:
                    result -= pow(num, int(polynomial[i][-1]))
            else:
                if len(polynomial[i]) == 1:
                    result -= int(polynomial[i])
                else:
                    co_x, power = polynomial[i].split('**')
                    co, x = co_x.split('*')
                    result -= int(co) * pow(num, int(power))

print(result == res)
