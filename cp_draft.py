
#Begin storyline: 

with open ("1_introduction.txt", "r", encoding = 'utf-8') as f:
    for i, line in enumerate(f,1):
        print(f"[i]: {line.rstrip()}")