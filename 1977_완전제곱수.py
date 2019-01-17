list_num = []
for i in range(2):
    list_num.append(int(input()))

list_multi = []
for j in range(1, 100+1):
    list_multi.append(j**2)

list_result = []
for z in range(list_num[0],list_num[1]+1):
    if z in list_multi:
        list_result.append(z)
if list_result == []:
    print('-1')
else:
    print(sum(list_result))
    print(min(list_result))
