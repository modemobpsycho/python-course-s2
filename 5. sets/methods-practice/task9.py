s = input().lower().split()

for i in range(len(s)):
    s[i] = s[i].strip(".,;:-?!")
    
set_word = set(s)
print(len(set_word))