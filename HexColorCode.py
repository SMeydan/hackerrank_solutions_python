size = int(input())
inside = False
color_list = []
hex_digits = '0123456789abcdefABCDEF'
for _ in range(size):
    user_input = input()
    if "{" in user_input:
        inside = True
    elif "}" in user_input:
        inside = False
    elif inside:
        input_list = user_input.split()
        for i in input_list:
            
            try:
                index = i.index('#')
                removed = i[index:]
                if ';' in i[index:]:
                    removed = i[index:].split(';')[0]
                if ',' in i[index:]:
                    removed = i[index:].split(',')[0]
                if ')' in i[index:]:
                    removed = i[index:].split(')')[0]
                if all(char in hex_digits for char in removed[1:]):
                    color_list.append(removed)
            except ValueError:
                pass
for i in color_list:
    print(i)
