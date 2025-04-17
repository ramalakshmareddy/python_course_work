while True:
    a,b,c=map(int,input("enter a,b,c ").split(","))
    if(a+b>c and a+c>b and b+c>a):
        print("triangle")
    else:
        print("not triangle")
            