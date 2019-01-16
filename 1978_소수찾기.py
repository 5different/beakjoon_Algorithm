ran_num = int(input())
num_list = list(map(int,input().split()))

count_sosu_pri = 0

for num in num_list:
    count_sosu = 0
    for j in range(1,num+1):
        if num%j == 0:
            count_sosu += 1
    if count_sosu == 2:
        count_sosu_pri +=1 
    
print(count_sosu_pri)


