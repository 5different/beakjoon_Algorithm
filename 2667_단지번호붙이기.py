T = int(input())

matrix = []
for testcase in range(T):
    num1 = list(input())
    matrix.append(num1)
x_len = len(matrix[0])
y_len = T
count = 0

visited =[[0]*x_len for i in range(y_len)]

def notwall(x,y):
    if x >= 0 and x < x_len and y >= 0 and y < y_len:
        return True 

def find(f_x,f_y):
    global count
    count += 1
    visited[f_x][f_y] = 1
    position = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in position:
        x = i[0]
        y = i[1]
        if notwall(f_x + x,f_y + y) and matrix[f_x + x][f_y + y] == '1' and not visited[f_x + x][f_y + y] :
            find(f_x + x,f_y + y)


result=[]
count2 = 0
for i in range(x_len):
    for j in range(y_len):
        if matrix[i][j] == '1'and not visited[i][j]:
            find(i,j)
            count2+=1
            result.append(count)
            count = 0
print(count2)
result2 = sorted(result)

for i in result2:
    print(i)

