import re
num = int(input())
for _ in range(num):
    user_input =input()
    try:
        if re.search(r'(?<!\\)\*\+|(?<!\\)\+\+|(?<!\\)\?\+', user_input):
            print('False')
        else:
            re.compile(user_input)
            print('True')
    except re.error:
        print('False')
