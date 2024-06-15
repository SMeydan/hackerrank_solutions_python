def print_formatted(number):
    for i in range(1,number+1):
        num,onum,bnum,hnum=i,oct(i),bin(i),hex(i)
        print(f"{num:>4}{onum[2:]:>5}{hnum[2:].upper():>5}{bnum[2:]:>5}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
