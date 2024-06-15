# Enter your code here. Read input from STDIN. Print output to STDOUT
size_e = int(input())
english = input()
size_f = int(input())
french = input()

english_set =set(english.split())
french_set =set(french.split())

print(len(english_set.symmetric_difference(french_set)))
