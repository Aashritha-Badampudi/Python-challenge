#To print a number which is repeated for max times in list
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

o=0
for i,j in d.items():
    if o<j:
        o=i
print(o)

