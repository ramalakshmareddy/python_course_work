products={"phones":20,"laptop":10,"watchs":5,"airpods":3,"Tv":0,"backpack":18,"kettle":0}

users={"ram":{"primememuber":"True","discount":"True","password":"ram@0393"},
       "saran":{"primememuber":"True","discount":"True","password":"saran@0393"},
       "rukku":{"primememuber":"True","discount":"False","password":"rukku@0393"},
       "prasanna":{"primememuber":"True","discount":"True","password":"prasanna@0393"},
       "anitha":{"primememuber":"False","discount":"False","password":"anitha@0393"}}
user_name=input("enter your name :")
password=input("enter you password :")
if users[user_name]["password"]==password:
    print("login success")
    print("items avilabile")
    for key in products:
        print(key)    

    slection=input("add you products:")
    stock=products[slection]
    if stock>0:
        print("stock avilabule")
        if (users[user_name]["primememuber"]=="True" and users[user_name]["discount"]=="True"):
            print("your a prime memuber you  get discount")
        elif(users[user_name]["primememuber"]=="True" and users[user_name]["discount"]=="False"):
            print("your a prime memuber")
        elif(users[user_name]["primememuber"]=="False" and users[user_name]["discount"]=="False"):
            print("your not a prime memuber tack mumbership get a discount ")        
    else:
        print("stock not avilabule ")    
else:
    print("enter valid user name and password")        