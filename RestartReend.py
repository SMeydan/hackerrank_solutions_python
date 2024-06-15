import re
string = input()
sub_string = input()
m = list(re.finditer(rf'(?={sub_string})', string))
if len(m) > 0:
    for i in m:
        print('(' + str(i.start())+ ", " + str(i.start() + len(sub_string) - 1) + ')')
else:
    print('(-1, -1)')
