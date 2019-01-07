A = int(input())
for i in range(1,A+1):
    str_2 = []
    for k in range(A+1-i,0,-1):
        str_2.append('*')       
    print(''.join(str_2))