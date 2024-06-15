s = input()
lower_arr, upper_arr, odd_arr, even_arr = [], [], [], []
for el in s:
    if el.isupper():
        upper_arr.append(el)
    elif el.islower():
        lower_arr.append(el)
    else:
        if int(el)% 2:
            odd_arr.append(el)
        else:
            even_arr.append(el)
lower_arr.sort()
upper_arr.sort()
odd_arr.sort()
even_arr.sort()
print(''.join(lower_arr + upper_arr + odd_arr + even_arr))
