#Two pointers swapping
a=[1,2,3,4,5]
low=0
high=len(a)-1
while low<high:
    a[low],a[high]=a[high],a[low]
    low+=1
    high-=1
print(a)