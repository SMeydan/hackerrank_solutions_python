#!/bin/python3

import math
import os
import random
import re
import sys


alphabet = "abcdefghijklmnoprsqtuvwxyz"
my_dict = {}
if __name__ == '__main__':
    s = input()

for letter in alphabet:
    len_letter = len(re.findall(letter, s))
    my_dict[letter] = len_letter

sorted_dict = sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))
for item in sorted_dict[:3]:
    print(f"{item[0]} {item[1]}")

