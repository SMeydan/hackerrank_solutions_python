from itertools import product

size, magnitude = map(int, input().split())
sqrt_mod = []

for _ in range(size):
    _, *current_list = map(int, input().split())
    sqrt_mod.append([x**2 % magnitude for x in current_list])
    
alls = product(*sqrt_mod)
total = max(sum(combination) % magnitude for combination in alls)
print(total)
