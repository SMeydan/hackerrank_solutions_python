cube = lambda x: x*x*x 

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    new_list = fibonacci(n - 1)
    new_list.append(new_list[-1] + new_list[-2])
    return new_list
    
