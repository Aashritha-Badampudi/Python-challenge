#Selection sort
a = [5,3,1,4,2]
for i in range(len(a)):
    pos=i
    mini=pos
    for j in range(pos,len(a)):
        if a[j] < a[mini]:
            mini = j
    a[mini],a[pos]=a[pos],a[mini]
print(a)