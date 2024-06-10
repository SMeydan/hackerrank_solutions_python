if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    students.sort(key=lambda x: x[1])
    second_note = sorted(set(x[1] for x in students))[1]
    second_note_guys = sorted(set(x[0] for x in students if x[1] == second_note))
    second_note_guys.sort()
    for student in second_note_guys:
        print(student)
