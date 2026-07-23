### deciaml to binary
n=int(input("enter a decimal:"))
op=""
while n!=0:
    r=n%2
    n=n//2
    op+=str(r)
op=op[::-1]    
print("the binary is:",op)    



## decimal to octal
# n=int(input())
# op=""
# while n!=0:
#     r=n%8
#     n=n//8
#     op+=str(r)
# op=op[::-1]    
# print("the octal is:",op)    


## decimal to hexadecimal
# n=int(input())
# op=""
# while n!=0:
#     r=n%16
#     n=n//16
#     op+=str(r)
# op=op[::-1]    
# print("the hexadecimal is:",op)    


# decimal to hexadecimal
# n=int(input())
# op=""
# hex="0123456789ABCDEF"
# while n!=0:
#     r=n%16
#     n=n//16
#     op+=hex[r]
# op=op[::-1]    
# print("the hexadecimal is:",op)


## binary to decimal

# n=int(input(""))

# op=0
# power=0
# while n!=0:
#     r=n%10
#     n=n//10
#     op=op+r*(2**(power))
#     power=power+1
# print(op)    


# ### octal to decimal

# n=int(input(""))

# op=0
# power=0
# while n!=0:
#     r=n%10
#     n=n//10
#     op=op+r*(8**(power))
#     power=power+1
# print(op)  


# ##hexdecimal to decimal


# n=input("")
# hex="0123456789ABCDEF"
# op=0
# power=0
# while n!=0:
#     r=n%10
#     n=n//10
#     op=op+hex[r]*(16**(power))
#     power=power+1
# print(op)  



# ##hexdecimal to decimal
# n=input("")
# POW=0
# hex="0123456789ABCDEF"
# value=0
# for i in n[::-1]:
#     value+=(hex.index(i)*(16**POW))
#     POW+=1   
    
# print(value)    


## binary to octal
# n=int(input(""))
# place=1
# op=""
# while n!=0:
#     r=n%100
#     n=n//100
#     s=str(r)
#     pow=0
#     t=0
#     for i in s[::-1]:
#         t+=int(i)*(2**pow)
#         pow+=1
#     op+=str(t)*place
#     place*10    
# print(op)        


## binary to octal

## binary to decimal to octal
n=int(input(""))     #--- binary-->decimal

op=0
power=0
while n!=0:
    r=n%10
    n=n//10
    op=op+r*(2**(power))
    power=power+1
print(op)    

output=""              #-->decimal to octal 
while op!=0:       
    r=op%8
    op=op//8
    output+=str(r)
output=output[::-1]    
print("the octal is:",output)    


### binary to hexa