#To print perfect square or not from a list:
l=list(map(int,input().split()))
for i in l:
    if (i**0.5)==int(i**0.5):
        print(i, "Perfect square")
    else:
        print(i, "Not a perfect square")