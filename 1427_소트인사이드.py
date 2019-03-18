A = list(map(int,input()))
A.sort(reverse = True)
pri_num ='' 
for i in A:
    pri_num += str(i)
print(pri_num)

