
def wrapper(f):
    def fun(l):
        formatted_numbers = ['+91 ' + number[-10:-5] + ' ' + number[-5:] for number in l]
        f(formatted_numbers)
    return fun

