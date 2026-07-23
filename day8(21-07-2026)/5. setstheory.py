'''
Sets:
---- 
-> It is a collection of data types. 
-> Indicated by { }
-> Do not allow duplicates
-> Mutable
-> Unordered(no positions)
'''

a={1,2,3,1}
# print(a[0])
print(a) #No duplicates printing
a.add(5)
print(a) #It is mutable
a.add(3)
print(a)
a={2,3,1}
a.pop()
print(a)
a={'a','b','c'}
a.pop()
print(a)
a={1,2,3}
a.discard(3)
print(a)
print(len(a))
a.discard(9)
print(a)
b={2,3,4,5}
b.remove(2)
print(b)
# b.remove(9)
# print(b)

a,b={1,2,3,4},{3,4}
print(a.intersection(b))
print(b.intersection(a))
print(a.union(b))
print(b.union(a))
print(a-b)
print(b-a)
print(b.issubset(a))
print(a.issuperset(b))