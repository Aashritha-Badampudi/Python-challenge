#To print product of the list
l=list(map(int,input().split()))
prod=1
for i in l:
    prod*=i
print(prod)