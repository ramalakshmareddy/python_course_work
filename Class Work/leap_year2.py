while True:
    stop=input("enter the y to continu(enter n to exit the loop) :")
    if(stop!="n"):
        year=int(input("enter the year: "))
        if(year%100==0 and year%400==0):
            print(year,"leap and century year")
        elif(year%400!=0 and year%4==0):
            print(year,"leap year but not a century year")
        else:
            print(year,"not a leap year")    
    else:
        break    