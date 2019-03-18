T = int(input())
N = [0]*100000
for i in range(T):
    idx,val = map(int,input().split())
    N[idx] = val

max_= 0
idx = 0
for i in range(100000):
    if max_ < N[i]:
        max_ = N[i]
        idx = i

for i in range(idx-1):
    if N[i] > N[i+1]:
        N[i+1] = N[i]

for i in range(100000-1,idx,-1):
    if N[i] >  N[i-1]:
        N[i-1] = N[i]
result = 0
for i in range(100000):
    result+= N[i]

print(result)






