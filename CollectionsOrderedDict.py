from collections import OrderedDict
n = int(input())
ordered_dictionary = OrderedDict()
for i in range(1, n+1):
    ord_list = input().split()
    name = " ".join(ord_list[:-1])
    price = int(ord_list[-1])
    if name in ordered_dictionary:
        ordered_dictionary[name] += price
    else:
        ordered_dictionary[name] = price

for name, price in ordered_dictionary.items():
    print(name, price)
