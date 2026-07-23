#To find chars which are vowels and at even position 
a="choti"
count=0
vow="aeiouAEIOU"
for i in range(len(a)):
    if i%2==0 and a[i] in vow:
        print(a[i])
        count+=1
print(count)

