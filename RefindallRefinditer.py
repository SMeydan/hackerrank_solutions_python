import re

text = input()
pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

match = re.findall(pattern, text)
if match:
    for group in match:
        print(group)
else:
    print(-1)
