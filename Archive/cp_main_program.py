from Archive.cp_draft428 import solo_adventure

#Begin Story
#Introduction
with open ("cp_1_introduction.txt", "r", encoding = 'utf-8') as f:
    for i, line in enumerate(f,1):
        print(f"[i]: {line.rstrip()}")


alone = solo_adventure