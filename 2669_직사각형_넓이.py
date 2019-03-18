
matrix = [[0]* 101 for i in range(101)]
for i in range(4):
    xs,ys,xe,ye= map(int,input().split())
    for x in range(xs,xe):
        for y in range(ys,ye):
            matrix[x][y] = 1 

count = 0 
for i in range(101):
    for j in range(101):
        if matrix[i][j] == 1:

            count += 1 
print(count)