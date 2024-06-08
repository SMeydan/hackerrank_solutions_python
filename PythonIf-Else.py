#!/bin/python3

import math
import os
import random
import re
import sys
def case(n):
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0 and ((n>2 and n<5 )or( 20<n)):
        print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    n = int(input().strip())
    case(n)
