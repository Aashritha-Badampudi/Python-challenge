#To find the second largest element in the list:
l=list(map(int,input().split()))
v=l[0]
for i in l:
    if i>v:
        v=i
l.remove(v)
v1=l[0]
for i in l:
    if i>v1:
        v1=i
print(v1)