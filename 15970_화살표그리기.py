T = int(input())

list_num = [0]*((10**5)+1)
for i in range(T):
    index , color = map(int,input().split())
    list_num[index] = color 

result = 0
for i in range(len(list_num)):
    if list_num[i] != 0:
        start = i
        cnt = 1
        while(1):
            if start-cnt >=0:   
                if list_num[start-cnt] == list_num[start] :
                    result += cnt
                    break
            if start+cnt <= 10**5:
                if list_num[start+cnt] == list_num[start] :
                    result += cnt
                    break 
            if start-cnt <0 and start+cnt >10**5:
                break
            cnt +=1
        
print(result)


