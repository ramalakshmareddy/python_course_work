while True:
  stop=input("enter y continu (enter n to exit the loop):")
  if(stop!="stop"):
        num1,num2,num3=input("enter the three numbers: ").split(",")
        if(int(num1)>int(num2) and int(num1)>int(num3)):
            print(num1,"is greatest")
        elif(int(num2)>int(num3)):
            print(num2,"is greatest")
        else:
            print(num3,"is greatest")
  else:
        break             