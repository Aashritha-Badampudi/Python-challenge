a="elephant"
v="aeiouAEIOU"

a=list(a)

l=0
h=len(a)-1

while l<h:
    if a[l] not in v:
        l+=1
    elif a[h] not in v:
        h-=1
    else:
        a[l],a[h]=a[h],a[l]
        l+=1
        h-=1
print("".join(a))