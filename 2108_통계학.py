for_range = int(input())
num_list = []
for i in range(for_range):
    num_list.append(int(input()))

print(round(sum(num_list)/for_range)) 
#반올림한 산술평균
 
def getmid(a):
    a.sort()
    return a[len(a)//2]

print(getmid(num_list))

w_count = {}
def find_vindo(a):
    for i in a:
        try: w_count[i] +=1 
        except: w_count[i] = 1
    max(w_count.values())
