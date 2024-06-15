user_input = input()
for_eval = user_input[user_input.find("(")+1 : user_input.rfind(")")]
print((eval(for_eval)))
