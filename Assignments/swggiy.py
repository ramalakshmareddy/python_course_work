#swiggy website modle
#users details
users={"ram":{"prime mumber":"True","password":"ram@0393","phone_number":"7036054598"},
       "sai":{"prime mumber":"True","password":"sai@07","phone_number":"8954506307"},
       "virat":{"prime mumber":"Flase","password":"virat@18","phone_number":"8089181818"},
       "gill":{"prime mumber":"Flase","password":"gill@97","phone_number":"80897979797"},
       "dinesh":{"prime mumber":"True","password":"dinesh@45","phone_number":"802454545"}}
#prime users resturants
prime_restaurant={"PistaHouse":{"Haleem":1000,"biryani":680,"Tandoori Chicken":750,"Murgh malai kabab":700},
                  "Paradise":{"birayni":1030,"paneer curry":1180,"chilli chicken":1200,"apollo fish":1980},
                  "ShahGhouse":{"dal fry":500,"mutton biryani":1850,"chicken biryani":1300},
                  "bawarchi":{"mutton kheema ":1550,"afghan chicken":1450,"mutton maharaja":1800},
                  "ITCKohenur":{"afgen chicken":1300,"mutton gosh":1850,"mutton afghani":1700}}



#normal users resturent
normal_restaurant={"hot bowl":{"chicken birayni":250,"mutton biryani":450,"roti":20,"panner curry":220},
                   "red biryani":{"chicken birayani":200,"afghan chicken":350,"dal fry":120,"rumali roti":30},
                   "blue star":{"veg noodles":120,"chicken maggi":150,"chicken noodles":170},
                   "mifel":{"chicken biryani":150,"mutton biryani":300,"chicken keema":200}}

#cheek users credentials
user=input("enter the name :").lower()
password=input("enter the password :")
if users[user]["password"]==password:
    print("welcome to swggiy ! order your fav iteams from your fav restaurant")
    if(users[user]["prime mumber"]=="True"):
        for i, (key, value) in enumerate(prime_restaurant.items(), start=1):
            print(f'{i}. {key} - ₹{value}')

    print(prime_restaurant['PistaHouse']["Haleem"])

            
""" print("Your Shopping Cart: ")


    elif(users[user]["prime mumber"]=="Flase"):
        for i,(key,value) in enumerate(normal_restaurant.items(),start=1):
            print(f"{i}.{key}-₹{value}")   """    