#To print even and odd elements in the list
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"odd")