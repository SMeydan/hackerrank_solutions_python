from collections import defaultdict
a_size, b_size = map(int, input().split())
a = defaultdict(list)
for i in range(a_size):
    inp = input()
    a[inp].append(str(i + 1))
for i in range(b_size):
    inp = input()
    if a[inp]:
        print(" ".join(a[inp]))
    else:
        print(-1)

