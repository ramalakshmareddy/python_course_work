n=int(input("enter the number :"))
total=0
if (100<= n <= 999):
    digit1=n//100
    digit2=(n//10)%10
    digit3=(n%10)
    total=digit1+digit2+digit3
print(total)    