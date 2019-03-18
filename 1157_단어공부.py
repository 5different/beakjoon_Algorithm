import sys 
word = sys.stdin.readline().upper()

def wordstudy(word):
    w_count = {}
<<<<<<< HEAD
    #리스트나 문자열에 들어있는 각 원소들의 개수를 카운트해서 
    #딕셔너리 형태로 만드는 방법 
    for i in word: 
        try: w_count[i] += 1
        except: w_count[i] = 1
    #파이썬 예외처리 방법을 이용하여 카운트
    #원소가 나올때마다 value의 값 한개씩 추가 
    #이렇게 하면 대신 '\n'도 인식을 함 그래서 완성된 딕셔너리에서 
    #'\n'을 제거해주면 좋음 
    
    del w_count['\n']

    key_comp = ''
    value_comp = 0

=======
    for i in word: 
        try: w_count[i] += 1
        except: w_count[i] = 1
    del w_count['\n']
    
    key_comp = ''
    value_comp = 0
    
>>>>>>> 7610b674acd0514cbe91e148a36da118b2f76155
    for key, value in w_count.items():
        if value > value_comp:
            value_comp = value
            key_comp = key
        elif value == value_comp:
            return '?'
    return key_comp 

print(wordstudy(word))
<<<<<<< HEAD

  

    


=======
>>>>>>> 7610b674acd0514cbe91e148a36da118b2f76155
    
    
