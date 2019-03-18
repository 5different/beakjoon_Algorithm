T = int(input())

for test in range(1,T+1):
    T2 = int(input())
    ma = []
    for t2 in range(T2):
        m = list(map(int,input().split()))
        ma.append(m)

    def not_wall(x,y):
        if x>=0 and x<T2 and y >=0 and y<T2:
            return True
    visited = [[0]*T2 for i in range(T2)]
    def find(x,y):
        global result 
        x_ = [0,1,0,-1]
        y_ = [1,0,-1,0] 
        for i in range(4):
            if ma[x+x_[i]][y+y_[i]] != 0 and not_wall(x+x_[i],y+y_[i]) and not visited[x+x_[i]][y+y_[i]] :
                visited[x+x_[i]][y+y_[i]] = 1
                if result < ma[x+x_[i]][y+y_[i]]:
                    result = ma[x+x_[i]][y+y_[i]]
                find(x+x_[i],y+y_[i])
        
    result = 0
    count = 0 
    for i in range(T2):
        for j in range(T2):
            if ma[i][j] != 0 and not visited[i][j]:
                visited[i][j] = 1
                find(i,j)
                count+= 1 
    
    print(count,result)


                
        