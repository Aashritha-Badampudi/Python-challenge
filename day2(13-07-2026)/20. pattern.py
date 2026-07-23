n=5
for i in range(1,n+1):
    if i==1 or i==5:
        print("* "*n)
    else:
        print("* "+(n-2)*"  "+"*")