while True:
    b=int(input("enter y (enter n to exit the loop)"))
    if b!=0:
       a=int(input("enter the number :"))
       if(a>1):
            for i in range(2,a):
                if(a%i==0):
                    print(a,"is not a prime number ")
                    break
            else:
             print(a,"prime number ")    
       else:
            print("not a prime number")
    else:
        break            