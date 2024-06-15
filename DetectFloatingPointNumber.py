num = int(input())
for _ in range(num):
    user_input = input()
    try:
        if '.' in user_input:
            float(user_input)
            print("True")
        else:
            print("False")
    except:
        print("False")
