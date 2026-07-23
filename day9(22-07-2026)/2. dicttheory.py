'''
* Dictionary:
--------------
-> Collection of data types
-> Denoted by { }
-> {item1, iten2, item3} Item = key, value pairs are present in items
Eg: dict={1:2,2;2,3:2,4:1} (a:b where a is key and b is value)
-> Mutable
-> Doesn't allow duplicate keys
-> It is ordered but not by position but by key
'''
dic={
     1:2,
     2:5,
     3:1,
     4:5
    }
print(len(dic))
dic[5]=1 #Syntax = dic[key]=value
print(dic)
dic[5]=3 #It updates
print(dic)
if 5 not in dic:
    dic[5]=1
else:
    dic[5]+=1
print(dic)
print(len(dic))

d={1:2,3:1,2:1,3:5}
print(d)

d.pop(2)
print(d)
print(dic.items())
dic.popitem()
print(dic)