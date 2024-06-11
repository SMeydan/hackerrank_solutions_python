
def split_and_join(line):
    sep = line.split(" ")
    new = ""
    for word in sep:
        new += word + "-"
    return new[:-1]
        
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
