elements=input("enter the elemnets :").split(" ")
frequency={}
for i in (elements):
    if (i in frequency):
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)            