if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    big_guy = arr[n-1]
    while(arr[n-1] == big_guy):
        if arr[n-1] != big_guy:
            break
        n -= 1
    
    print(arr[n-1])
