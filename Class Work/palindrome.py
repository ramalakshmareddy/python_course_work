while True:
    a=input("enter y to continu (enter n to exit ):")
    if(a!="n"):
      option=int(input("select option :"))
      num=int(input("enter the numebr :"))
      org=num
      revers=0
      if(option==1):
          while num>0:
             digit=num%10
             revers=revers*10+digit
             num=num//10
          if(revers==org):
            print("palindrome")
          else:
            print("not palindrome")
    else:
       break
         
         
