n=3
for i in range(1,n+1):
    print("  "*i+" *"*((n+1)-i)+" *"*(n-i))

n-=1
for i in range(1,n+1):
    print("  "*((n+1)-i)+" *"*((2*i)+1))