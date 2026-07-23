#To remove duplicates in the list using set
l=[1,2,3,4,5,2]
l=set(l)
print(l)

s={1,2,3,4,5}
s=list(s)
print(s)

l1=list(map(int,input().split()))
print(set(l1))