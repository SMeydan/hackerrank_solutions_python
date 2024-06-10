if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        user_input = input()
        if user_input[0] == 'i':
            _, position, p_int = user_input.split()
            arr.insert(int(position), int(p_int))
        elif user_input[0:2] == 'pr':
            print(arr)
        elif user_input[0:3] == 'rem':
            _, p_int = user_input.split()
            arr.remove(int(p_int))
        elif user_input[0] == 'a':
            _, p_int = user_input.split()
            arr.append(int(p_int))
        elif user_input[0] == 's':
            arr.sort()
        elif user_input[0:2] == 'po':
            arr.pop()
        elif user_input[0:3] == 'rev':
            arr.reverse()
