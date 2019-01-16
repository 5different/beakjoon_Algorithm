num = list(map(int,input().split()))
num_list = []

for i in range(num[0],num[1]+1):
    count_sosu = 0
    if i%2 == 1:
        for j in range(1,i+1):
            if j%2 == 1:
                if i%j == 0:
                    count_sosu +=1
                    if count_sosu >2:
                        count_sosu = 0
                        break 
                    
    if count_sosu == 2:
        print(i)



