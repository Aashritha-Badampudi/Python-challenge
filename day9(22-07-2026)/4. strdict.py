a="Honey Aashritha"
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)