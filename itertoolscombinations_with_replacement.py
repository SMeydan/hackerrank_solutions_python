from itertools import combinations_with_replacement

word, num = input().split()
listed = []
for i in combinations_with_replacement(sorted(word), int(num)):
    print(''.join(i))
