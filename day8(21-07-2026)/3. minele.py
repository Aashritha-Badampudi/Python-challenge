l=list(map(int,input().split()))
v=l[0]
for i in l:
    if i<v:
        v=i
print(v)