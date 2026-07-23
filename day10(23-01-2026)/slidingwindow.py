a="sadbustsad"
b="sad"
c=0
l=len(b)
for i in range(0,len(a)-l+1):
    if a[i:i+l]==b:
        c+=1
print(c)