T = int(input())
# 2차원 배열을 만들고 
# 각 행값+1은 회원을 뜻함 
# 행의 각 원소들은 그 행에 해당하는 회원과 친구인 사람들임 
#   
metrix = []
for i in range(T+1):
    metrix.append([])

while(1):
    A,B = map(int,input().split())
    if A and B == -1:
        break
    else:
        metrix[A].append(B)
        metrix[B].append(A)
print(metrix)

   
