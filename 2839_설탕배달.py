num = int(input())

if num%5  == 0 :
    print(int(num/5))
else :
    if((num-3)%5 == 0 and num-3 >= 0):
        print(int((num-3)/5)+1)
    elif((num-6)%5 == 0 and num-6 >= 0):
        print(int((num-6)/5)+2)
    elif((num-9)%5 == 0 and num-9 >= 0):
        print(int((num-9)/5)+3)
    elif((num-12)%5 == 0 and num-12 >= 0):
        print(int((num-12)/5)+4)
    else:
        print(-1) 