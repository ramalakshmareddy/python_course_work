def prime(val):
    is_prime=0
    for i in range (2,(val//2)+1):
        if val%i==0:
            is_prime+=1
    if is_prime>1:
        print("not a prime number ") 
    else:
        print("is a prime number ")
val=int(input("enter the number :"))
prime(val)                   

