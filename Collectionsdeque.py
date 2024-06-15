from collections import deque
num = int(input())
d = deque()
for _ in range(num):
    user_input = input().split()
    if user_input[0] == 'append':
        num2 = user_input[1]
        d.append(num2)
    if user_input[0] == 'appendleft':
        num2 = user_input[1]
        d.appendleft(num2)
    if user_input[0] == 'pop':
        d.pop()
    if user_input[0] == 'popleft':
        d.popleft()

print(" ".join(list(d)))
