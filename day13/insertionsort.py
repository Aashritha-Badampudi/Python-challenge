#Insertion sort
a=[5,1,3,4,2]
for i in range(1,len(a)):
    ele=a[i]
    j=i-1
    while j>=0 and a[j]>ele:
        a[j+1]=a[j]
        j-=1
    a[j+1]=ele
print(a)