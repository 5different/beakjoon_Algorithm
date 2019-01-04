def ex1000():
    # 두개의 수를 한번에 입력받아서 이를 합하여 출력하는 코드
    a,b = map(int, input().split())
    # 그냥 더하게 되면 문자열 단위로 더해지기 때문에 정수화 하여 더한다 
    print(a+b)

def ex1001():
    # 두개의 수를 한번에 입력받아서 이를 빼고 출력하는 코드
    a,b = map(int, input().split())
    print(a-b)

def ex10172():
    # 개 모양의 문자배열을 그대로 출력하는 코드 
    # |\_/|
    # |q p|   /}
    # ( 0 )"""\
    # |"^"`    |
    # ||_/=\\__|
 
 
    print('|\_/|')
    print('|q p|   /}')
    print('( 0 )"""\\') # \를 출력하고 싶다면 \를 한개 더 써야한다 
    print('|"^"`    |')
    print('||_/=\\\\__|')


def ex10430():
    #첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.
    A,B,C = map(int, input().split())
    print('{}\n{}\n{}\n{}'.format((A+B)%C,(A%C + B%C)%C,(A*B)%C,(A%C * B%C)%C))


def ex2839():
    #3 6 9 12 즉 최대 3kg인것은 나머지가 존재할때 4개를 최대로 쓴다.
    A = int(input())
    if(A%5 == 0):
        print(A/5)
    else:
        for i in range(1,4):
            if((A-3*i)%5 == 0):
                if(A-3*i >= 0):
                    print(((A-3*i)/5)+1*i)
                else:
                    print('-1')
                
        # if((A-3)%5 == 0):
        #     if(A-3 >= 0):
        #         print(((A-3)/5)+1)
        #     else:
        #         print('-1')
        # elif((A-6)%5 == 0):
        #     if(A-6 >= 0):
        #         print(((A-6)/5)+2)
        #     else:
        #         print('-1')
        # elif((A-9)%5 == 0):
        #     if(A-9 >= 0):
        #         print(((A-9)/5)+3)
        #     else:
        #         print('-1')
        # elif((A-12)%5 == 0):
        #     if(A-12 >= 0):
        #         print(((A-12)/5)+4)
        #     else:
        #         print('-1')
        

