#To print the sum of elements in list of a window size
a=[1,2,3,4,5]
w=2
for i in range(0,len(a)-w+1):
    sum=0
    for j in a[i:i+w]:
        sum+=j
    print(sum, end=" ")