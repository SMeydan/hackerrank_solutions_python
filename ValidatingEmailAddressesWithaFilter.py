import re
def fun(s):
    pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
    return re.match(pattern, s)

