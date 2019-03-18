T =  int(input())

result = 0
r = 0
for i in range(T+1):
    N =[T,T-i]
    while(1):
        if N[-2] - N[-1] < 0:
            break
        else:
            N.append(N[-2] - N[-1])
    if len(N) > result:
        result = len(N)
        r = i

N = [str(T), str(T - r)]
while (1):
    if int(N[-2]) - int(N[-1]) < 0:
        break
    else:
        N.append(str(int(N[-2]) - int(N[-1])))

print(result)
print(' '.join(N))




