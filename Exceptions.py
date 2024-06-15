size = int(input())
for _ in range(size):
    a, b = input().split()
    try:
        result = int(a)/int(b)
        print(int(result))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: " + str(e))
