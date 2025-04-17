while True:
    a=input("enter y to continu(enter n toexit the loop):")
    if(a!="n"):
        b=int(input("enter the number"))
        if(b%2==1 and b>0):
            print(b,"is positive and odd")
        elif(b%2==1 and b<0):
            print(b,"it is odd but nagitive number") 
        elif(b%2==0 and b>0):
            print(b,"is positive but not odd number")
        else:
            print(b,"not positive and not odd number")
    else:
        break            
