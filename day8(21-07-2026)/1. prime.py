l=list(map(int,input().split()))
o=[]
for i in l:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        o.append(i)
print(o)