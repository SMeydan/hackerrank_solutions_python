def count_substring(string, sub_string):
    position = 0
    repeat = 0
    while position != -1:
 
        position = string.find(sub_string,position)

        if position == -1:
            break
            
        position = position + 1
        repeat += 1    
          
    return repeat  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
