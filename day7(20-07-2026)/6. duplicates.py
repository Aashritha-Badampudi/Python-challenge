#To remove duplicate elements in the list
l=list(map(int,input().split()))
lst=[]
for i in l:
    if i not in lst:
        lst.append(i)
print(lst)