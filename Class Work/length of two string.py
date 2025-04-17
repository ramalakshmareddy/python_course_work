while True:
    stop=int(input("enter 1 to continu (enter 0 to exit the loop) :"))
    if(stop!=0):
        str_1,str_2=input("enter string1 :").split(",")
        if(len(str_1)>len(str_2)):
            print("first string is longer")
        elif(len(str_1)==len(str_2)):
            print("both strings equal")
        else:
            print("second string is longer")        
    else:
        break    