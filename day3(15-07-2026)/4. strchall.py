#To print all chars in string along with index
a="python"
for i in a:
    print((a.index(i)),i)

print("********")

b="Python"
for i in range(0,len(b)):
    print(i,b[-(i+1)])

print("*********")

for i in range((len(a)-1),-1,-1):#Decrementing and last -1 is to include 0
    print(i,a[i])