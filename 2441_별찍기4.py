A = int(input())
for i in range(1,A+1):
    str_2 = []
    for j in range(i-1):
        str_2.append(' ')
    for k in range(A+1-i,0,-1):
        str_2.append('*')       
    print(''.join(str_2))