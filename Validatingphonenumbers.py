import re
regex_pattern = r"^(7|8|9)(\d){9}$"
for _ in range(int(input())):
    if (bool(re.match(regex_pattern, input()))):
        print('YES')
    else:
        print('NO')
    
