size = int(input())
for i in range(size):
    size_arr = int(input())
    arr = list(map(int, input().split()))
    is_valid = True
    big_guy = float('inf')
    while size_arr > 0:
        if arr[-1] >= arr[0]:
            if arr[-1] <= big_guy:
                big_guy = arr[-1]
                arr.pop(-1)
            else:
                is_valid = False
                break
        else:
            if arr[0] <= big_guy:
                big_guy = arr[0]
                arr.pop(0)
            else:
                is_valid = False
                break
        size_arr -= 1
    print('Yes') if is_valid else print('No')

        
        
