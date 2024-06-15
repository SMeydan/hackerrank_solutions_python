def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        new_str = ""
        for i in substring:
            if i not in new_str:
                new_str += i
        
        print(new_str)
        

