n=int(input("enter the number :"))
sum=0
for i in range(2,(n//2)+1):
    prime=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime+=1
            break
    if prime ==0:
        print(i)
        sum+=i
print("sum",sum)            


         

