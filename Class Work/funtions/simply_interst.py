def cluculte(price,rate,time):
    sum=(price*rate*time)/100
    return sum
price=float(input("enter the price :"))
rate=float(input("enter the rate :"))
time=float(input("enter the time :"))
intrest=cluculte(price,rate,time)
print(intrest)