#Positive slicing
a="Honeyy"
print(a[2])
#print(a[5]) #IndexOutofBound error
print(a[0:3])
print(a[:4])
print(a[1:4])
print(a[0:],a[:6],a[0:6],a)
print(a[1:])
print(a[1:6:2]) #It is know as step #Prints odd indexes
print(a[0: :2])#Prints even indexes

#Negative indexing
b="Navya"
print(b[-3])
print(b[-5:-2])
print(b[:-2])
print(b[-5:-2:1])
print(b[-3:])
print(b[::-1])

#Mixed indexing
c="Aashritha"
print(c[-6:5])
print(c[2:-3])

#Reverse order
print(b[::-1])