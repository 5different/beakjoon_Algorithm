str_ten = input()
str_len = len(str_ten)/10

i = 0 
for i in range(0,int(str_len)+1):
     print(str_ten[0+10*i:10+10*i])