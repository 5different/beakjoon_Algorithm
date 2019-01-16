import operator
ran_num = int(input())

li_words =[]
for i in range(ran_num):
    li_words.append(input())

dic_num = {}
for i in li_words:
    try : dic_num[i] = len(i)
    except :  dic_num[i] = 0

sortedArr = sorted(dic_num.items(), key=operator.itemgetter(1, 0))
# [('e', 1), ('ry', 2), ('yy', 2), ('yyyy', 4)] --> 출력결과물 

for i in sortedArr:
    print(i[0]) 
 

