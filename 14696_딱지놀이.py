
T = int(input())
for test in range(T):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A_list = [0]*5
    B_list = [0]*5

    for i in range(1,len(A)):
        if A[i] == 4:
            A_list[A[i]] +=1
        elif A[i] ==3:
            A_list[A[i]] += 1
        elif A[i] ==2:
            A_list[A[i]] += 1
        elif A[i] ==1:
            A_list[A[i]] +=1

    for i in range(1,len(B)):
        if B[i] == 4:
            B_list[B[i]] += 1
        elif B[i] == 3:
            B_list[B[i]] += 1
        elif B[i] == 2:
            B_list[B[i]] += 1
        elif B[i] == 1:
            B_list[B[i]] += 1

    result = 0
    if A_list[4] > B_list[4]:
        result = 'A'
    elif A_list[4] == B_list[4]:
        if A_list[3] > B_list[3]:
            result = 'A'
        elif A_list[3] == B_list[3]:
            if A_list[2] > B_list[2]:
                result = 'A'
            elif A_list[2] == B_list[2]:
                if A_list[1] > B_list[1]:
                    result = 'A'
                elif A_list[1] == B_list[1]:
                    result ='D'
                else:
                    result = 'B'
            else:
                result = "B"
        else:
            result = "B"
    else:
        result = 'B'

    print(result)

