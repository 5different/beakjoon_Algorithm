import sys 
word = sys.stdin.readline().upper()

def wordstudy(word):
    w_count = {}
    for i in word: 
        try: w_count[i] += 1
        except: w_count[i] = 1
    del w_count['\n']
    
    key_comp = ''
    value_comp = 0
    
    for key, value in w_count.items():
        if value > value_comp:
            value_comp = value
            key_comp = key
        elif value == value_comp:
            return '?'
    return key_comp 

print(wordstudy(word))
    
    
