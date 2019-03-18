T = int(input())
for test in range(1,T+1):
    T2, N = map(int,input().split())
    ma =[]
    for i in range(T2):
        m = list(map(int,input().split()))
        ma.append(m)
    dt = T2 - N
    rrr = 100000000
    result = 0
    if dt >=0:
        for x in range(N//2,N//2+dt+1):
            for y in range(N//2,N//2+dt+1):
                L = ma[x][y]+ma[x-1][y-1]+ma[x+1][y+1]  
                R = ma[x][y]+ma[x-1][y+1]+ma[x+1][y-1]
                result = abs(L-R)
                print(result)
                if result < rrr:
                    rrr = result 
        
    print(rrr)