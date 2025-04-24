menu={"chicken biryani":210,
      "mutton biryani":253,
      "chilli chicken":264,
      "chicken 65":264,
      "veg.biryani":154,
      "paneer 65":196,
      "tandoori roti":40,
      "rumali roti":40}
option={1:"chicken biryani",2:"mutton biryani",3:"chilli chicken",4:"chicken 65",5:"veg.biryani",6:"paneer 65",7:"tandoori roti",8:"rumali roti"}
print("Welcome to 12table restaurant")
for i,(items,price) in enumerate( menu.items(),start=1):
 print(f"{items}:Rs{price}")
items=list(map(int,input("enter the item no :").split(" ")))
order_list={}
for i in(items):
  if(i in order_list):
    order_list[i]+=1
  else:
    order_list[i]=1   
for key,value in order_list.items():
   menu_item=option[key]
   price=menu[menu_item]
   order_total=price*value
   print(f"{menu_item}x {value}=RS{order_total}")
total=0   
for key,value in order_list.items():
   menu_item=option[key]
   price=menu[menu_item]
   total +=price*value
GST=total*0.18
your_bill=total+GST

print(your_bill)
print("Thank you for Dining with us!")
print("Have a Nyc Day !")     





