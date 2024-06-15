

maxdepth = 0
def depth(elem, level=-1):
    global maxdepth
    current_level = level + 1
    if current_level > maxdepth:
        maxdepth = current_level
    for child in elem:
        depth(child, current_level)

    return maxdepth

