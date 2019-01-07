A = int(input())

num = input().split()

for i in range(0,A):
    num[i]=int(num[i])    
sc_max = max(num)
for i in range(0,A):
    num[i]=num[i]/sc_max*100
aver = sum(num)

print(aver/A)
    