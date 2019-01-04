def ex2741():
    A = int(input())
    for i in range(1,A+1):
        print(i)

def ex2742():
    A = int(input())
    for j in range(A,0,-1):
        print(j)

def ex2739():
    A = int(input())
    for i in range(1,10):
        print("{} * {} = {}".format(A,i,A*i))


def ex2438():
    
    A = int(input())
    for i in range(1,A+1):
        str_2 = []
        for j in range(0,i):
            str_2.append('*')        
        print(','.join(str_2))
 
def ex2439():
    
    A = int(input())
    for i in range(1,A+1):
        str_2 = []
        for k in range(A-i,0,-1):
            str_2.append(' ') 
        for j in range(0,i):
            str_2.append('*')        
        print(''.join(str_2))

def ex2440():
    
    A = int(input())
    for i in range(1,A+1):
        str_2 = []
        for k in range(A+1-i,0,-1):
            str_2.append('*')       
        print(''.join(str_2))

ex2440()