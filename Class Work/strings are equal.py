while True:   
   a,b=input("enter the first string :").split(",")
   c=int(input("enter any number (you enter 0 exit the loop:)"))
   if c!=0: 

      if a==b:
         print("both strings are equal")
      else:
        print("not equal")
        
   else:
      break    
        