

N,X = map(int,input().split())
num = input().split()

better_num = ''
for i in range(0,N):
    if(int(num[i])<X):
        better_num = better_num + num[i] + ' '

print(better_num)




