from itertools import combinations

user_input = input().split()
word = sorted(user_input[0])
per_num = int(user_input[1])
pers = []
result = []
for i in range(1, per_num+1):
    pers = list(combinations(word, i))
    for per in pers:
        result.append((''.join(per)))
        
for per in result:
    print(per)
