import re
user_input = input()
pattern = r'([a-zA-Z0-9])\1'
matches = re.findall(pattern, user_input)
try:
    print(matches[0])
except:
    print(-1)
