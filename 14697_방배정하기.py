A,B,C,N = map(int,input().split())

result = 0
def room():
    global result
    for i in range(N+1):
        tempC = C*i
        for j in range(N+1):
            tempB = B * j
            for t in range(N+1):
                tempA = A * t
                if tempA+tempB+tempC == N:
                    result = 1
                    return
room()
print(result)
