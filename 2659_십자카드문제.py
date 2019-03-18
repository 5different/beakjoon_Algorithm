num = list(input().split())
list_n = []

for i in range(4):
    t = num.pop(0)
    num.append(t)
    A = []
    for i in range(len(num)):
        A.append(num[i])
    B = int(''.join(A))
    list_n.append(B)

mins = 10000
for i in range(4):
    if list_n[i] < mins:
        mins = list_n[i]
count = 1

result = []
for i in range(1111,10000):

    if '0' not in str(i) and i not in result:   
        if i == mins:
            break 

        count += 1
        tte = []
        te = []
        for j in str(i):
            te.append(j)

        for i in range(4):
            ttte = te.pop(0)
            te.append(ttte)
            A = []
            for i in range(len(te)):
                A.append(te[i])
            B = int(''.join(A))
            tte.append(B)
        
        result.extend(tte) 

print(count)  






    