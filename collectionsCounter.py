from collections import Counter

num_of_shoes = int(input())
shoe_list = Counter(list(map(int, input().split())))
num_of_customers = int(input())
total = 0
for i in range(num_of_customers):
    size, money = input().split()
    if shoe_list[int(size)]:
       shoe_list[int(size)] -= 1
       total += int(money)

    
print(total)
