#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    sp_s  = s.split(" ")
    sp_c = ""
    for word in sp_s:
        sp_c += word.capitalize() + " " 
    return str(sp_c)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
