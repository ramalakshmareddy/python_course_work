def removeing():
    n=list(map(int,input("enter the numebrs :").split()))
    removeing_numebr=int(input("enter the remove numeber :"))
    new_list=[]
    for i in range (len(n)):
        
        if removeing_numebr!=n[i]:
            new_list.append(n[i])
    
    print(new_list)        
removeing()