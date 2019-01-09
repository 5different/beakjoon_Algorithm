import sys

alpa_num = sys.stdin.readline().split()

print_index=''
for i in alpa_num[1]:
    for j in range(1,int(alpa_num[0])+1):
        print_index += i 

print(print_index) 
