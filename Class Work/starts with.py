while True:
    a=int(input("enter 1 to continu (enter 0 to exit the loop)"))
    if(a!=0):
        b=input("enter the string").lower()
        velow="aeiou"
        if(b[0] in velow):
            print("string starting with velow")
        else:
            print("string not starting with velow")
    else:
        break            