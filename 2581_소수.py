first_num = int(input())
second_num = int(input())


count_sosu_pri = []
for num in range(first_num,second_num+1):
    count_sosu = 0
    for j in range(1,num+1):
        if num%j == 0:
            count_sosu += 1
    if count_sosu == 2:
        count_sosu_pri.append(num)
if len(count_sosu_pri):
    print(sum(count_sosu_pri))
    print(min(count_sosu_pri))
else:
    print('-1')