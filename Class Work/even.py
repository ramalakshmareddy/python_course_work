option=int(input("enter option 1 or 2 :"))
num=int(input("enter the numer :"))
if(option==1):
    for i in range(1,num+1):
        if (i%2==0):
            print(i)
if(option==2):
    for i in range(2,num+1,2):
        print(i)
        



