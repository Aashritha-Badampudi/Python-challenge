a="elephant"
v="aeiouAEIOU"
a=list(a)
v=list(v)
# print(a,"\n",v)
l=0
h=len(a)-1
while l<h:
    if l is v:
        a[l],a[h]=a[h],a[l]
        l+=1
    if h is v:
        a[l],a[h]=a[h],a[l]
        h-=1
print("".join(a))