#To print even position charecter of a string
a="Aashritha"
for i in range(0,len(a),2):
    print(i,a[i])
print("********")
for i in range(len(a)):
    if i%2==0:
        print(i,a[i])