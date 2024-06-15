# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_notes, length = map(int, input().split())
notes = []
averages = [0]*num_of_notes
for i in range(length):
    notes = input().split()
    for y in range(num_of_notes):
       averages[y] += float(notes[y])

for n in averages:
    print(n/length)
