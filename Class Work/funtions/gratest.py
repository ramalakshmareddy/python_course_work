while True:
    n1,n2=input("enter the 2 numbers(enter the stop stop)").split(" ")
    if(n1!="stop stop"):
        print("1.greatest")
        print("2.smallest")
        op=int(input("select option :"))
        if(op==1):
            if(int(n1)>int(n2)):
                print(n1,"is greater")
            else:
                print(n2,"is greater")
        elif(op==2):
            if(int(n1)<int(n2)):
                print(n1,"is smallest") 
            else:
                print(n2,"is smallest")
        else:
            print("choose correct op")
    else:
        break                              