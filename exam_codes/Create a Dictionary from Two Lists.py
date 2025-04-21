keys=list(map(str,input("enter the keys sparated by space :").split(" ")))
value=list(map(str,input("enter the keys sparated by space :").split(" ")))
result={}
for i in range(len(keys)):
    result[keys[i]]=value[i]
print(result)

