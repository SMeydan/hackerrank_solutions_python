len_set, len_ab = map(int, input().split())
the_set = input().split()
happiness = set(input().split())
unhapiness = set(input().split())
hp_score, uhp_score = 0, 0
for el in the_set:
    if el in happiness:
        hp_score += 1
    if el in unhapiness:
        uhp_score += 1
print(hp_score - uhp_score)
