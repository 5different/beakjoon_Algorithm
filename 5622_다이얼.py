input_string = input()

dial_dict = {'1': '00', '2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ','0':'00'}

key_string= '' 
for i in input_string:
    for key,value in dial_dict.items():
        if i in value: 
           key_string += key
result = 0
for i in key_string:
    result += int(i)+1

print(result) 


