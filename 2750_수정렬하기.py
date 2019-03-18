
range_num= int(input())

num_list = []
for i in range(range_num):
    num_list.append(int(input())) 

for i in (sorted(num_list)):
    print(i)
