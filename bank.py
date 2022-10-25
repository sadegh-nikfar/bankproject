import mysql.connector
import random
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='bank',
)
mycursor = mydb.cursor()

class user:
    id_number = 0
    name = ""
    family = ""
    age = 0
    deposit = 0
    def create_account(self):
        self.id_number = random.randint(10_000, 99_999)
        self.name = input("please enter your name:")
        self.family = input("please enter your family:")
        self.age = input("please enter your age:")
        self.deposit = int(input("please enter your amount deposit:"))
        print("\n\n Account created")
        print("\n\n Account Id Number: ",self.id_number)

        
        
    def show_account(self):
        print("number id:",self.id_number)
        print("username:",self.name)
        print("family:",self.family) 
        print("age:",self.age) 
        print("deposit:",self.deposit)
    def deposit_account(self):
        amount = int(input("please enter amoumt deposit:"))
        self.deposit += amount
        print("your amount account:",self.deposit)     
    def withraw_account(self):
        withraw = int(input("please enter your withrawll amount:"))
        if withraw <= self.deposit:
            self.deposit = self.deposit - withraw
            print("your amount account:",self.deposit)
        else:
            print("your not amount ")  
    def show_balance(self):
        return self.deposit        
              


bank = user()                
input_user =""
num = 2
while num != 0:
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2.  SHOW ACOOUNT DETAILS")
    print("\t3. DEPOSIT AMOUNT")
    print("\t4. WITHDRAW AMOUNT")
    print("\t5. SHOW BALANCE")
    print("\tSelect Your Option (1-5) ")
    input_user = input()
    if input_user == "1":
        bank.create_account()
        sql = "INSERT INTO user (`id`,`name`, `family`, `age`, `deposit`) VALUES (%s, %s, %s, %s, %s)"
        val = (bank.id_number,bank.name,bank.family,bank.age,bank.deposit)
        mycursor.execute(sql,val)
        mydb.commit()
    elif input_user == "2":
        bank.show_account() 
    elif input_user == "3":
        bank.deposit_account()  
        update ="UPDATE user SET deposit = (%s) WHERE Name ='sadegh'"
        update_value = (bank.deposit)
        mycursor.execute(update_value)
        mydb.commit() 
    elif input_user == "4":
        bank.withraw_account()    
    elif input_user == "5":
        bank.show_balance()    
    else:
        print("Invalid choice")  
        input_user = input("Enter your choice : ")  
        
         

    


           
        