set1=set(map(int,input("enter the numbres :").split()))
set2=set(map(int,input("enter the numbres :").split()))
common=[]
for i in set1:
    if i in set2:
      common.append(i)
print(common)      

