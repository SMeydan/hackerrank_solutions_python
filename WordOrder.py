# size = int(input())
# words = []
# string = ""
# for _ in range(size):
#     word = input()
#     for wrds in words:
#         if word == wrds[0]:
#             wrds[1] += 1
#             break
#     else:
#         words.append([word, 1])
        
# for word, count in words:
#     string += str(count) + " "
# print(len(string)//2)
# print(string)

size = int(input())
words = {}
string = ""
for _ in range(size):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for count in words.values():
    string += str(count) + " "
print(len(words))
print(string)
