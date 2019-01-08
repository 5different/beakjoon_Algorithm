A = int(input())
B = int(input())
C = int(input())

multi = str(A*B*C) 
  
for i in range(0,10):
    t = multi.count(str(i)) #문자열에서 원소의 개수를 셀때 사용
    print(t)
    

