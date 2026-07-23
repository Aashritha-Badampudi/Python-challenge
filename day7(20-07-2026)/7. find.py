# l=list(map(int,input().split()))
# T=int(input())
# for i in l:
#     if i==T:
#         print(True)
#         break
#     else:
#         print(False)
#         break

#Other method
l=list(map(int,input().split()))
T=int(input())
F=False
for i in l:
    if T==i:
        F=True
print(F)