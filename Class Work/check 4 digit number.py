while True:
    a=input("enter y to continu (enter n to exit)")
    if(a!="n"):
       print("1.op is str method \n2.op is numaric method")
       op=int(input("choose the option"))
       num=int(input("enter the numebr :"))
       if(op==1):
          if (num%2==0 and len(str(num))==4):
             print(num,"is even and 4 digit number")
          elif(num%2==0 and len(str(num))!=4):
             print(num,"even number but not a 4 digit number")
          elif(num%2!=0 and len(str(num))==4):
             print(num,"not even numebr but it a 4 digit number")
          else:
             print(num,"not a even number not 4 digit number")
       elif(op==2):
          if(num%2==0 and (999<num>10000)):
              print(num,"is even and 4 digit number")
          elif(num%2==0):
              print(num,"even number but not a 4 digit number")  
          elif((num%2!=0 and (999<num>10000))):
              print(num,"not even numebr but it a 4 digit number")
          else:
             print(num,"not a even number not 4 digit number")
       else:
          print("choose correct option")       
    else:
       break       


