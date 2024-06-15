from collections import Counter

group_size = int(input())
inp = list(map(int, input().split()))

inp_count = Counter(inp)
captain = next(i for i, count in inp_count.items() if count == 1)

print(captain)
