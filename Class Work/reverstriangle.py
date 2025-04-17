n=int(input("enter the number :"))
for i in range(n):
    spces=(" "*(n-i))
    for j in range(i+1):
        print(spces+"*",end="")
    print()    