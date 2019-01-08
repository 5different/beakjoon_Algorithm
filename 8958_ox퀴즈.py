count = int(input())

ox = []
score_count = 0
for i in range(0,count):
    ox.append(input())
    
for j in range(0,count):
    delete_X = ox[j].split("X") 
    # X값을 삭제하고 O값들의 리스트를 만듬
    sum_all = 0

    for z in delete_X: 
        #리스트 내의 한 문자열식 돌림
        sum_O = 0
        
        for i in range(1,z.count('O')+1): 
            # 한 문자열에서 O의 개수를 N이라고 하면 N의 정수까지의 합을 구하기 위한 포문
            sum_O +=i    # N의 정수까지의 합 
        sum_all +=sum_O  # sum_O의 합 
    print(sum_all)     




            


