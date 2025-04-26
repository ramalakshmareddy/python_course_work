def movie(items):
    for i in items:
        yield i
items=[{"telugu_movies":["pokiri","RRR","Bahubali","URI","Anima","Pushpa:"]},{"hindi":["Dangal","Jawan","Pathaan","Bajrangi Bhaijaan"]},{"kannada":["kgf","kantara"]}]
ob=movie(items)
print(next(ob))
status=1
while True:
    status=int(input("enter 1 to next and 0 to exit :"))
    if status:
        print(next(ob))
    else:
        break    
