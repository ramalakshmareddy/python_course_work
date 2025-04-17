while True:
    stop=int(input("enter 1 to continu(enter o to exit) :"))
    if(stop!=0):
        num=int(input("enter the number :"))
        if((50 <num<100) and(num%5==0)):
            print(num,"in range and divigibule by 5")
        elif((50 < num>100)):
            print(num,"in range but not divigibule by 5") 
        elif((num%5==0)):
            print(num,"not in range but divigible by 5")    
        else:
            print(num,"not in range and not divigibule by 5")     
    else:
        break