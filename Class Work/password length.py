while True:
    stop=int(input("enter 1 continu (enter 0 to exit loop) :"))
    if(stop!=0):
        password=input("enter the password :")
        if(len(password)>=8):
            print("strong password")
        else:
            print("choose strong password")
    else:
        break            
