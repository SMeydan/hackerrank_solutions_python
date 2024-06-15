from datetime import datetime
import os
def time_delta(t1, t2):
    frm = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, frm)
    dt2 = datetime.strptime(t2, frm)
    return str(int(abs(dt1-dt2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
