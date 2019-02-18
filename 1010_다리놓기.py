T = int(input())

for testcase in range(T):
    first,second = map(int,input().split())
    
    first_num = second - first 
    blank = first_num + 1
    count = 0
    for z in range(first-1):
        for i in range(first_num,0,-1):
            for j in range(i,0,-1):
                count +=1
                blank+=j
    print(count)        
    print(blank)
    

    
     

