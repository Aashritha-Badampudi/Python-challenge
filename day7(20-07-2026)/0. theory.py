## collection of diff data type
# --> []
## to store a group of date in in sigle variable
## colletion of different data types
## List allows duplicates


### printing index wise
a=[1,2,3,4,5,"python"]
## there python is called an element it prints whole word but not a single charecter
print(a[1])
print(a[5])


## list keyword

# 1.len()       --->finding of lenght
print(len(a))

# 2..append()   -->add element added at last with index
a.append(5)
print(a)

# 3 .insert()    -->add element at a particular position
a.insert(3,"honey")
print(a)

##Adding duplicates
a.append(5)
print(a)

## 4 .pop()
a.pop()
print(a)

b=[1,2,2,3,4,4,5]
b.pop(2)
print(b)

## 5 .remove()
b.remove(4)
print(b)

## 6 .index()
print(b.index(2))

# print(find(b[6])) Returns only in string not in list

##7 min() and max()
a=[1,2,2,3,4.5,5]
print(min(a))
print(max(a))

##8. sum()
print(sum(a))

## .count()
print(a.count(2))
print(a.count(6))

## sorted(name of list)
b=[4,3,1,2]
b=sorted(b)
print(b)

## .clear()
b.clear()
print(b)

## del()
del(b)
# print(b)

#User input
# Take list input from the user
# n=6
# l=[]
# for i in range(n):
#     b=int(input())
#     l.append(b)
# print(l)

# #Other method
# l=list(map(int,input().split()))
# print(l)

#String input
# s=list((input().split()))
# print(s)

#To print the output
a=[1,2,3,4]
print(a)
print(*a)
for i in range(0,len(a)):
    print(i,a[i])
for i in a:
    print(i)

'''
1. List allow duplicates
2. List is ordered
3. List is mutable
'''