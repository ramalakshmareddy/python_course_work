n=int(input("enter the numeber :"))
for i in range(1,n+2):
      if (i<=((n+1)//2)):
            print("* "*i)
      else:
            print("* "*(n-i+2))      