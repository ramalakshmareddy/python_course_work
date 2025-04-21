num=list(map(int,input("enter the numbers :").split()))
tem=[]
for i in (num):
    if i not in tem:
        tem.append(i)
print(tem)        