while True:
    stop=int(input("enter 1 continu(enter 0 to exit) :"))
    if(stop!=0):
       num1,num2=input("enter two numbers (separeted with , )").split(",")
       sum=(int(num1)+int(num2))
       if(sum%2==0):
           print("sum is even ")
       else:
           print("sum is not even")     
    else:
        break    