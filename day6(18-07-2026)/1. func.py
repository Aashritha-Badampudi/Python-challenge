# function:
# a peice of code which ws written seperatlly and executed when it is called
## instead of writting a code many time

## 4 types
# 1.no parameter passing and no return type
## 2. no parameter parsing and with return
## parameter passing and no return type
## parameter passing and with return


## no parameter passing  no return passing
# def addition(): 
#     a=int(input())
#     b=int(input())  #-->parameter passing
#     c=a+b
#     print(c)

# addition()    #---> paramet     


# ## 2. no parameter parsing and with return
# def addition():
#     a=int(input())
#     b=int(input())   
#     c=a+b
#     return c   
# print(addition())


# 3. with parameter passing  no return passing
# def addition(a,b):
#     print(a+b)
# a=int(input())
# b=int(input())        
# d=addition(a,b)
# print(d)    #--->none


# # 4. with parameter passing  with return passing
# def addition(a,b):
#     c=a+b
#     return c

# a=int(input())
# b=int(input())        
# print(addition(a,b))




# ## example

# ## no parameter passing  no return passing
# #3 wap to find given number is prime or not
def prime_no():
    a=int(input())
    count=0 
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        print("prime")  
    else:
        print("not")          
prime_no()  

#  2. no parameter parsing and with return
def prime_no():
    a=int(input())
    count=0 
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        return "prime" 
    else:
        return "not"        
print(prime_no())  



# 3. with parameter passing  no return passing
def prime_no(a):
    
    count=0 
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        print("prime")  
    else:
        print("not")   
a=int(input())           
prime_no(a)  

# 3. with parameter passing   return passing
def prime_no(a):
    
    count=0 
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        return "prime"
    else:
        return "not" 
a=int(input())           
print(prime_no(a))