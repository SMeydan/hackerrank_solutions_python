import re
pattern = r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[A-Za-z0-9]{10}$'
num = int(input())
for _ in range(num):
    if bool(re.match(pattern, input())):
        print('Valid')
    else:
        print('Invalid')
