import numpy
user_input = list(map(int, input().split()))
inp_tup = tuple(user_input)
print(numpy.zeros(inp_tup, dtype=int))
print(numpy.ones(inp_tup, dtype=int))

