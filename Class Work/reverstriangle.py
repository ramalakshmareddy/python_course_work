n=int(input("enter the number :"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("* ",end="")
    print()        