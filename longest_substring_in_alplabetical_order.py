longest=""
temp=""
prev=""
for i in s:
    if i>=prev:
        temp=temp+i
        prev = i
    elif i<prev:
        prev=i
        temp=i
    if len(temp)>len(longest):
            longest=temp
print("Longest substring in alphabetical order is: "+longest)
