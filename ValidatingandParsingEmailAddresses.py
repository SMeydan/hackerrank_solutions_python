import email.utils
import re
regex_pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
num = int(input())
for _ in range(num):
    name, emailx = email.utils.parseaddr(input())
    if (bool(re.match(regex_pattern, emailx))):
        print(email.utils.formataddr((name, emailx)))
