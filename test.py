for_range = int(input())
num_list = []
for i in range(for_range):
    num_list.append(int(input()))

w_count = {}
def find_vindo(a):
    for i in a:
        try: w_count[i] +=1 
        except: w_count[i] = 1
    
    comp_v = 0
    comp_k = 0
    for keys, values in items(w_count):
        if values >= comp_v:
            comp_v = values
            comp_k = keys
    if comp_k in 


     



print(find_vindo(num_list))