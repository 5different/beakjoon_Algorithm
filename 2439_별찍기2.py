A = int(input())
for i in range(1,A+1):
    str_2 = []
    for k in range(A-i,0,-1):
        str_2.append(' ') 
    for j in range(0,i):
        str_2.append('*')        
    print(''.join(str_2))