num, user_input = int(input()), list(map(int, input().split()))
positive = all(x > 0 for x in user_input)
print('True') if positive and any(str(num) == str(num)[::-1] for num in user_input) else print('False')
