A, B = input().split(" ")

day_str1 =['SUN','MON','TUE','WED','THU','FRI','SAT']
day_str2 =['31','28','31','30','31','30','31','31','30','31','30','31']

month = int(A)
day = int(B)

count=0
for i in range(0,month-1):
    count = count + int(day_str2[i])
day_count =(count + day)%7
print(day_str1[day_count])