
def sum_digit(number):
    A = sum([int(i) for i in str(number)])
    return A + number


delete=[]
origin=[]
for i in range(1,10000+1):
    if sum_digit(i) <= 10000: 
        delete.append(sum_digit(i)) #리스트내에 특정값 추가하는 방법
    origin.append(i)

delete_ex = list(set(delete)) #리스트내 중복값 제거하는 방법

for i in delete_ex:
    origin.remove(i) # 리스트내에 특정값 제거하는 방법

for i in origin:
    print(i)







