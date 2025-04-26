def listing(a):
    d=[]
    for i in (a):
     double=i*2
     d.append(double)
    return d
a=list(map(int,input("enter the numbers :").split()))
result=listing(a)
print(result)