menu={"chicken biryani":210,
      "mutton biryani":253,
      "chilli chicken":264,
      "chicken 65":264,
      "veg.biryani":154,
      "paneer 65":196,
      "tandoori roti":40,
      "rumali roti":40}
print("Welcome to 12table restaurant")
for items,price in menu.items():
 print(f"{items}:Rs{price}")
order_total=0


while True:
    items=input("enter what you want: ")
    if(items=="done"):
      break
    if items in (menu):
       order_total+=menu[items]
       print(f"your  item{items}. has been add orderd:") 
    else:
       print(f"your orderd {items} is not avalibule")
Gst=order_total*0.10
bill=order_total+Gst
print("your final bill is Rs{:.2f}".format(bill))
print("Thank you for Dining with us!")     





