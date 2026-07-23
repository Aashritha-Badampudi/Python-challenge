'''
* Tuple:
---------
-> Collection of data types
-> Denoted by () Eg: a=(1,2,3)
-> Immutable
-> Allows duplicates
-> Ordered(allows positions)
'''

#Keywords
a=(1,2,3,1)
print(a)
print(a[1])
#print(a.append(4)) #Doesn't work coz it's immutable
print(len(a))
print(a.count(1))
print(a.count(9))
print(a.index(3))
print(a.index(1))
# print(a.index(9))
# print(a.find(9)) it works only in the list
print(min(a))
print(max(a))
print(sorted(a))
print(sum(a))