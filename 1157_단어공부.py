import sys 
word = sys.stdin.readline() 
new_word = ''
for i in word:
    if 97 <= ord(i) <= 97+25:
         new_word += chr(ord(i)-32)
    else:
        new_word += i 

n = 0
w = 0
for i in ''.join(set(new_word)):
    if new_word.count(i) >= n:
        if w is not '?':
            n = new_word.count(i)
            w = i 
        else:
            w = '?' 

print(w)
        
    
    
