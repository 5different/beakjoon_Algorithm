input_num = list(input().split())

for idx, vla in  enumerate(input_num):
    input_num[idx]= int(vla[::-1])

print(max(input_num))