#To print no. of uppercase letters in a string
a="PythON"
count=0
for i in a:
    if i.isupper()==True:
        count+=1
print(count)