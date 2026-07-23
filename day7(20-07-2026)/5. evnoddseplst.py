#To print even and odd in list seperately
l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)