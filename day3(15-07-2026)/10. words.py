#To find the no. of words in the string
a="Python is a progr@m"
count=0
for i in a:
    if " " in i:
        count+=1
print("The no. of words in the string are :",(count+1))