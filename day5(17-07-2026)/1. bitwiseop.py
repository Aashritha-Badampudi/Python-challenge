# ## bitwise operator (binary bits)

# # 1.bit wise and(&)
#     # return 1  when all bits are 1
#     # return o when even one bit is 0
   
#     # #   b1  b2    0/p
#     #      1   1     1
#     #      1   0     0
#     #      0   1     0
#     #      0   0     0


# ### logical   
# ## bit wise we use in number


# ## 2 .bit wise or(|)
# ##  return 1  when any wit is one
# ##   retur 0 when ll bits are zero

#      #   b1  b2    0/p
#     #      1   1     1
#     #      1   0     1
#     #      0   1     1
#     #      0   0     0

# ### 3 bitwise not operator 

# # # n=int(input())
# # n2=int(input())
# # print(~n2)

# ##3 bitwise ~(not)operator


# ## bitwise  XOR


# ## bitwise leftshif

# #3 bitwise rightshift

# ## wap to print 2 pow10 without using (**)
# n1=2
# out=n1<<9
# print(out)


# ## wp to print given number is even or odd using bitwise operators
# # n=input("")
# # if n[-1]=="0":
# #     print("even")
# # else:
# #     print("odd")    

# n=int(input())
# if n&1==0:
#     print("even")
# else:
#     print("odd")


## wap to find the LSB bit in given

# n=int(input("enter a decimal:"))
# op=""
# while n!=0:
#     r=n%2
#     n=n//2
#     op+=str(r)
# op=op[::-1]    
# print("the lsb is:",op[-1])


# n=int(input())
# if n&1==0:
#     print("0")
# else:
#     print("1")



## write a program to find the nth position bitin the given number
# n=int(input())
# pos=int(input()) 
# if n>>pos:
#     print(n&1)


## left shift
# n=int(input())
# p=int(input())
# p=p<<p
# if(n&p):
#     print("1")
# else:
#     print("0")


## wap to set nth position bit in the given number
## set means making a number to 1
## reset means making number to 0


 

## wap to reset nth position bit in the given number


# n = int(input())
# p = int(input())
# c=~(1<<p)
# r=n &c
# print(r)


## wap to toggle nth posistion bit in the 
# n = int(input())
# p = int(input())
# c=(1<<p)
# r=n^c
# print(r)

## 2nd method
 


# n = int(input())
# p = int(input())

# print(n ^ (1 << p))


## wap to print 2,s complete of a numbers
n=int(input())
print((~(n))+1)

## problem

# 1. Check if number is Even or Odd  
#    Ex: 5 -> Odd, 8 -> Even Use n & 1






# 2. Check if Nth bit is Set or Not  
#    Ex: 5=101, 2nd bit=0 Use (n >> n) & 1
# 3. Set Nth bit  
#    Ex: 5=101, set 2nd bit -> 111=7 Use n | (1 << n)
# 4. Clear Nth bit  
#    Ex: 7=111, clear 2nd bit -> 101=5 Use n & ~(1 << n)
# 5. Toggle Nth bit  
#    Ex: 5=101, toggle 1st bit -> 111=7 Use n ^ (1 << n)
# 6. Turn off rightmost set bit  
#    Ex: 12=1100 -> 1000=8 Use n & (n-1)
# 7. Turn on rightmost 0 bit  
#    Ex: 8=1000 -> 1001=9 Use n | (n+1)
# 8. Check if number is Power of 2  
#    Ex: 16->Yes, 18->No Use n & (n-1) == 0
# 9. Multiply by 2  
#    Ex: 5 -> 10 Use n << 1
# 10. Divide by 2  
#     Ex: 10 -> 5 Use n >> 1
# 11. Multiply by 8  
#     Ex: 3 -> 24 Use n << 3
# 12. Get absolute value without if  
#     Ex: -5 -> 5 Use (n ^ (n>>31)) - (n>>31)
# 13. Find 1's Complement  
#     Ex: 5=101 -> 010=2 Use ~n
# 14. Find 2's Complement  
#     Ex: 5 -> -5 Use ~n + 1
# 15. Swap two numbers without temp  
#     Ex: a=5,b=3 -> a=3,b=5 Use a=a^b^a