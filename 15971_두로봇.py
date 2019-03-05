T,start,end = map(int,input().split())

matrix = [[0]*(T+1) for i in range(T+1)]
matrixlength = [[0]*(T+1) for i in range(T+1)]
visit = [[0]*(T+1) for i in range(T+1)]

for i in range(T-1):
    l, r, length = map(int,input().split())
    matrix[l][r] = 1
    matrix[r][l] = 1
    matrixlength[l][r] = length 
    matrixlength[r][l] = length 

number = []
list_result =[]

def DFS(x):
    number.append(x)
    for i in range(1,T+2):
        if i > T:
            number.pop()
        else:
            if matrix[x][i] == 1 and not visit[x][i] :
                visit[x][i] = 1
                visit[i][x] = 1
                if i == end:
                    number.append(i)
                    for i in number:
                        list_result.append(i)
                    return 
                else:
                    DFS(i) 

DFS(start)

newnumber = [] 
for i in range(len(list_result)-1):
    newnumber.append(matrixlength[list_result[i]][list_result[i+1]])

count = len(newnumber)-1
new = [] 
for z in range(len(newnumber)):
    result = 0
    for i in range(len(newnumber)):
        if i == count:
            continue
        result += newnumber[i]
    new.append(result)
    count -= 1    

print(min(new))