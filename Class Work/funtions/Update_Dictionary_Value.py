def update_value():
    dict_value=eval(input("enter the values :"))
    key=input("enter the keys :")
    new_value=input("enter the new value :")
    if new_value.isdigit():
        new_value=int(new_value)
    if key in dict_value:
        dict_value[key]=new_value
        print(dict_value)
    else:
        print("key not found dic")   
update_value()     