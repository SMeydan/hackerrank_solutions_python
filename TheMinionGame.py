def minion_game(string):
    stuart, kevin = 0, 0
    length = len(string)

    for i in range(length):
        if string[i] in 'AEIOU':
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif kevin < stuart:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
