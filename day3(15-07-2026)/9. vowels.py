#To find no. of vowels in a string
a="Navya Burrewar"
count=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        count+=1
print("The no. of vowels are:",count)

vow="aeiouAEIOU"
c=0
for i in a:
    if i in vow:
        c+=1
print("No. vowels are:",c)