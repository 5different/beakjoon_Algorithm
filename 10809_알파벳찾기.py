sentence = list(input()) 
#문자열을 문자단위로 한개씩 리스트화 시키는 방법

alpa = []
alpaclone = []
for i in range(97,97+26):
    alpa.append(chr(i))  
    alpaclone.append(chr(i)) 


string_new = []
for t in sentence:
#문자열 중복요소 검사후 변경 중복되는것이 있으면 이후'!'로 변경 
    if t not in string_new:
        string_new.append(t)
    else:
        string_new.append('!')
    
for z in alpa:
    if z in string_new:
        alpa[alpa.index(z)] = str(string_new.index(z))

new_print=''
for x in alpa:
    if x in alpaclone:
        new_print += '-1 '
    else:
        new_print += (x+' ')
                 
print(new_print)


        
    

    