while True:
    n=int(input("enter the number :"))
    if n!=0:
        if(n%3==0 and n%7==0):
            print(n,"is divisible 3 and 7")
        elif(n%3==0):
            print(n,"is divisibule 3 only")
        elif(n%7==0):
            print(n,"is divisible 7 only")
        else:
            print(n,"not divisiblue")
    else:
        break                    