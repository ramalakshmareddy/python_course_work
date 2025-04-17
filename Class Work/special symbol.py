while True:
    a=int(input("enter 1 to continu(enter 0 to exit ) :"))
    if(a!=0):
        in_put=input("enter the input")
        symbol="!@#$%^&*"
        if(in_put in symbol):
            print("special character")
        else:
            print("not a special character")
    else:
        break            