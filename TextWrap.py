import textwrap

def wrap(string, max_width):
    position = 0
    new_str = ""
    while(position < len(string)):
        if len(string) - position < int(max_width):
            new_str += string[position :]
            return new_str
        new_str += string[position : (position + int(max_width))] + "\n" 
        position += int(max_width)
        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
