A,B,C = map(int,input().split(" "))
num = [A,B,C]

maxValue=max(num)
num.remove(maxValue)
secondValue = num[0]
for i in range(1,len(num)):
    if secondValue < num[i]:
        secondValue = num[i]

print(secondValue)