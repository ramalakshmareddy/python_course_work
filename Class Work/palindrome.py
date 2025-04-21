while True:
    a=input("enter y to continu (enter n to exit ):")
    if(a!="n"):
      option=int(input("select option :"))
      num=int(input("enter the numebr :"))
      org=num
      revers=0
      if(option==1):
          while num>0:
             revers=revers*10+(num%10)
             num=num//10
          if(revers==org):
            print("palindrome")
          else:
            print("not palindrome")
      elif(option==2):
         if(str(num)==str(num)[::-1]):
             print("palindrome")
         else:
            print("not palindrome")     
    else:
       break
         
         
