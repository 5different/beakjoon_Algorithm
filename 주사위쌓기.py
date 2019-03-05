T = int(input())
m = []
for i in range(T):
    N  = list(map(int,input().split()))
    m.append(N)

    # 1 6 -> 2345
    # 2 4 -> 1365
    # 3 5 -> 1264
    # 4 2 -> 1365
    # 5 3 -> 1264
    # 6 1 -> 2345
print(m)
x_ = [0,1,2,3,4,5]
y_ = [5,3,4,1,2,0]

f = [[],[2,3,4,5],[1,3,6,5],[1,2,6,4],[1,3,6,5],[1,2,6,4],[2,3,4,5]]

state = [0]*len(m)
for tt in range(1):
    Bot = m[0][x_[tt]]
    Top = m[0][y_[tt]]
    state[0] = tt+1
    count = 1
    while(1):
        for j in range(6):
            if m[count][j] == Top:
                Bot = m[count][j]
                Top = m[count][y_[j]]
                state[count] = j+1
                count += 1
                print(Bot,Top)
                break
        if count == len(m):
            break
    result = 0

    print(state)
    count = 0
    for i in state:
        max_ = 0
        for j in range(4):
           if max_ <  m[count][ f[i][j] ]:
               max_ = m[count][ f[i][j] ]
        result += max_
        count += 1

    print(result)











