def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    for i in range(size -1, 0, -1):
        s = "-".join(alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(4*size-3, "-"))
    for i in range(size):
        s = "-".join(alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(4*size-3, "-"))
    s_rug = '\n'.join(lines)
    print(s_rug)
    return s_rug

        
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
