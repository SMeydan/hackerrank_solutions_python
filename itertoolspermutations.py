from itertools import permutations

user_input = input().split()
word = user_input[0]
per_num = int(user_input[1])
result = []
pers = list(permutations(word, per_num))
for per in pers:
    result.append((''.join(per)))

for per in sorted(result):
    print(per)
