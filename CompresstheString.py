from itertools import groupby
g_string = input()
for key, value in groupby(g_string):
    print("(" + str(len(list(value))) + ", " + str(key) + ")", end=" ")
