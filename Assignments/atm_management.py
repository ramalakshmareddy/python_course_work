#creating user credentials
user_name = "ram"                                    #user name
user_password = "Ram@0393"                           #user password

#taking user inputs
customer_name = input("Enter your name: ")           #customer name
customer_password = input("Enter your password: ")   #customer password

#checking valid customer or not 
if (customer_name == user_name and customer_password == user_password):
    print("Welcome to bank")                          #greating
    amount = 1000
    
    while True:                                       #while loop for loopeing contusely untill get exit
        print("\n1. Deposit\n2. Withdraw\n3. Mini Statement\n4. Exit") #menu
        option = int(input("Enter your choice (1-4): ")) #user input
        
        if (option == 1):
            deposit = int(input("Enter amount to deposit: "))
            amount += deposit
            print("Your transaction is successful")
            print("Total amount:", amount)
           
        elif (option == 2):
            withdraw = int(input("Enter amount to withdraw: "))
            if (amount >= withdraw):
                amount -= withdraw
                print("Your transaction is successful")
                print("Total amount:", amount)
            else:
                print("Insufficient Funds")
                
        elif (option == 3):
            print("Account Holder:", user_name)
            print("Current Balance:", amount)
            
        elif (option == 4):
            print("Thank you for choosing us")
            break
            
        else:
            print("Invalid option. Please try again.")
            
else:
    print("Invalid credentials")

                
        
   

    





