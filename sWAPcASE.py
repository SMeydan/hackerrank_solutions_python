def swap_case(s):
    new_s = ""
    for ch in s:
        if ch.isupper() :
            new_s += ch.lower()
        elif ch.islower() :
            new_s += ch.upper()
        else:
            new_s += ch
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
