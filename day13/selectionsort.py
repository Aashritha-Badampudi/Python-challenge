#Selection sort
a = [5,3,1,4,2]
for j in range(len(a)):
    pos=j
    mini=pos
    for i in range(pos,len(a)):
        if a[i] < a[mini]:
            mini = i
    a[mini],a[pos]=a[pos],a[mini]
print(a)