import mysql.connector
import random
import datetime
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
        date = datetime.datetime.now()
        self.id_number = random.randint(10_000, 99_999)
        self.name = input("please enter your name:")
        self.family = input("please enter your family:")
        self.age = input("please enter your age:")
        self.deposit = int(input("please enter your amount deposit:"))
        print("\n\n Account created")
        print(date)
        print("Account Id Number: ",self.id_number)
        

        
        
    def show_account(self):
        # id_input = input("please enter account number:")
        # if id_input == self.id_number:
            print("number id:",self.id_number)
            print("username:",self.name)
            print("family:",self.family) 
            print("age:",self.age) 
            print("deposit:",self.deposit)
        # else:
        #     print("Invalid Choice")    
        
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
        print("your account amount:",self.deposit)      
    def exit_progrram(self):
        return exit()          
              


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
    print("\t6. EXIT PROGRRAM")
    print("\tSelect Your Option (1-6) ")
    input_user = input()
    if input_user == "1":
        bank.create_account()
        sql = "INSERT INTO user (`id`,`name`, `family`, `age`, `deposit`) VALUES (%s, %s, %s, %s, %s)"
        val = (bank.id_number,bank.name,bank.family,bank.age,bank.deposit)
        mycursor.execute(sql,val)
        mydb.commit()
    elif input_user == "2":
        id_input = input("please enter account number:")
        sql = "SELECT * FROM user WHERE id = %s"
        value = (id_input,)
        mycursor.execute(sql,value)
        myresult = mycursor.fetchall()
        for x in myresult:
         print(x)
         
        
    elif input_user == "3":
        id_input = input("please enter account number:")
        bank.deposit_account()  
        update ="UPDATE user SET deposit = (%s) WHERE id =%s"
        update_value = (bank.deposit,id_input,)
        mycursor.execute(update_value)
        mydb.commit() 
    elif input_user == "4":
        bank.withraw_account()    
    elif input_user == "5":
        bank.show_balance()
    elif input_user == "6":
        bank.exit_progrram()         
    else:
        print("Invalid choice")  
        input_user = input("Enter your choice : ")  
        
         

    


           
        