def average(array):
    set_height = set(array)
    sums = sum(set_height)
    num = len(set_height)
    return sums/num

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
