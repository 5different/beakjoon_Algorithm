score = []
re = 40
for i in range(0,5):
    A = int(input())
    if 100 >= A >40:
        score.append(A) 
    else:
        score.append(re)
print(int(sum(score)/5))
    

        
