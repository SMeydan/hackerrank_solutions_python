if __name__ == '__main__':
    s = input()
    s1,s2,s3,s4,s5 = False,False,False,False,False
    for ch in s :
        if(ch.isalnum()):
            s1 = True
        if(ch.isalpha()):
            s2 = True
        if(ch.isdigit()):
            s3 = True
        if(ch.islower()):
            s4 = True
        if(ch.isupper()):
            s5 = True
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
