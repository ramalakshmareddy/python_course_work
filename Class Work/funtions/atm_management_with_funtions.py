data={"balance":50000,"transaction":[]}

def withdraw(amount):
    if amount<=data["balance"]:
      data["balance"]-=amount
      data['transaction'].append(f'{amount} withdrawn from your account.')
      print("Amount is succesfully withdrawn.")
def depoist(amount):
   data["balance"]+=amount
   data["transaction"].append(f"{amount} depoist for your account .")
   print(f"{data["balance"]} is dipoist your account")
def Check_Balance():
    print(f"Your current balance is {data['balance']}")
  
def view_transaction():
    for i in data['transaction']:
        print(i)
print("welcome to ATM")

while True:
   print(f"1.withdraw\n2.depoist\n3.Check_Balance\n4.view_transaction\n5.exit")
   option=int(input("enter the selection (1-5)"))
   if (option==1):
      amount=int(input("enter the withdraw amount :"))
      withdraw(amount)
   elif(option==2):
        amount=int(input("enter the depoist amount :"))
        depoist(amount)
   elif(option==3):
        Check_Balance()
   elif(option==4):
       view_transaction()
   elif(option==5) :
       print("see you later")
       break  
   else:
       print("Try Again") 
       
    

 