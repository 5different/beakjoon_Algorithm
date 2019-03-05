import random
T = int(input())
matrix = [["0"]*T for i in range(T)]

i = 0 
j = 0
def find():
    global i,j
    while(1):
        flag = 0
        a = random.randint(0,T-1)
        for x in range(T):
            if matrix[i][x] == a:
                flag = 1 
                break
        for x in range(T):
            if matrix[x][j] == a:
                flag = 1
                break
        if flag == 0:
            matrix[i][j] = a

            if 
            
            break
        


                
        
print(matrix)  

                
    