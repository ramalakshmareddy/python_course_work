n=int(input("enter the numeber :"))
count=0
for i in range(1,n+1):
    if(i%5==0):
        print(i)
        count+=1
print("count",count)        
