while True:
    a=input("enter y to continu (enter n to exit the loop) ")
    if (a!="n"):
        b=int(input("enter the numeber :"))
        if ((b%2==0 or b%3==0) and(b%2!=0 and b%3!=0)): 
            print(b,"divisible 2 and 3 but not both")
        elif((b%2==0 and b%3==0)):
            print(b,"divisible 2 and 3 ")    
        elif(b%2==0):
           print(b"divisible 2 only")
        elif(b%3==0):
            print(b,"divisible 3 only")
        else:
            print(b,"not divisible 2 and 3 ") 
    else:
        break                 