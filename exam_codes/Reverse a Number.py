n=int(input("enter the number :"))
revers=0
while n>0:
    digit=n%10
    revers=revers*10+digit
    n=n//10
print(revers)    