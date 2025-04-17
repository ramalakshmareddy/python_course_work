while True:
    a=input("enter y to continu(enter n to exit loop)")
    if(a!="n"):
        temperature=int(input("enter temperature :"))
        if(temperature<15):
            print("Cold")
        elif(15<=temperature<=30):
            print("moderate") 
        else:
            print("Hot")
    else:
        break               
