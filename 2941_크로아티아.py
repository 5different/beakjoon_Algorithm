cro_string = input()
cro_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count = 0

for i in cro_list:
    if i in cro_string: 
        cro_string = cro_string.replace(i,'A')

print(len(cro_string))