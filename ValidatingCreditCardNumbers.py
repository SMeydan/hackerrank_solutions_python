import re
size = int(input())
pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"

for _ in range(size):
    valid = 1
    card = input()
    
    if ' ' in card:
        valid = 0
    
    elif not (card[0] == '4' or card[0] == '5' or card[0] == '6'):
        valid = 0
        
    if '-' in card:
        if not re.findall(pattern, card):
            valid = 0
        card = card.replace('-', '')
        
    for i in range(len(card) - 3):
        if card[i] == card[i+1] == card[i+2] == card[i+3]:
            valid = 0
    
    if not len(card) == 16:
        valid = 0
    
    print("Valid") if valid else print("Invalid")
