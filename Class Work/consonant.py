while True:
    a=int(input("enter 1 to continu (enter 0 to exit the loop) :"))
    if (a!=0):
        b=input("enter the latter :").lower()
        vowle="aeiou"
        if(b not in vowle):
            print(b,"is consonant")
        else:
            print(b,"not a consonant")
    else:
        break            