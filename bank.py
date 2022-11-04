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
        self.date = datetime.datetime.now()
        self.id_number = random.randint(10_000, 99_999)
        self.name = input("please enter your name:")
        self.family = input("please enter your family:")
        self.age = input("please enter your age:")
        self.deposit = int(input("please enter your amount deposit:"))
        print("\n\n Account created")
        print(self.date.strftime("%x"))
        print("Account Id Number: ",self.id_number)
                        
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
        print("your account amount:",self.deposit)      
    def exit_progrram(self):
        return exit()       
              

welcome = input("Do you have an account? (y/n)")
bank = user()                
input_user =""

while welcome == "n":
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    print("\t\t\t\t\tMAIN MENU")
    print("\t\t\t\t\tNEW ACCOUNT")
    bank.create_account()
    sql = "INSERT INTO user (`id`,`name`, `family`, `age`, `deposit` , `date` ) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (bank.id_number,bank.name,bank.family,bank.age,bank.deposit,bank.date.strftime("%x"))
    mycursor.execute(sql,val)
    mydb.commit()
    bank.exit_progrram()

while welcome == "y":
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    print("\tMAIN MENU")
    print("\t1.  SHOW ACOOUNT DETAILS")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. SHOW BALANCE")
    print("\t5. EXIT PROGRAM")
    print("\tSelect Your Option (1-5) ")
    input_user = input()
    
    if input_user == "1":
        # bank.show_account()
        id_input = input("please enter account number:")
        sql = "SELECT * FROM user WHERE id = %s"
        value = (id_input,)
        mycursor.execute(sql,value)
        myresult = mycursor.fetchall()
        for x in myresult:
         print("number id:",x[0])
         print("username:",x[1])
         print("family:",x[2]) 
         print("age:",x[3]) 
         print("deposit:",x[4])
         print("account date created:",x[5])
         
        
    elif input_user == "2":
        # bank.deposit_account()
        id_input = input("please enter account number:")
        user_deposit = int(input("please enter your amount:"))
        sql = "SELECT * FROM user WHERE id = %s"
        value = (id_input,)
        mycursor.execute(sql,value)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x[4])
            id_deposit = x[4]
        deposit = id_deposit + user_deposit
        # bank.deposit_account()  
        update ="UPDATE user SET deposit = %s WHERE id = %s"
        update_value = (deposit,id_input)
        mycursor.execute(update,update_value)
        mydb.commit() 
        print('your balance account:',deposit)
    elif input_user == "3":
        # bank.withraw_account()  
        id_input = input("please enter account number:")
        user_deposit = int(input("please enter your amount:"))
        sql = "SELECT * FROM user WHERE id = %s"
        value = (id_input,)
        mycursor.execute(sql,value)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x[4])
            id_deposit = x[4]
        deposit = id_deposit - user_deposit
         
        update ="UPDATE user SET deposit = %s WHERE id = %s"
        update_value = (deposit,id_input)
        mycursor.execute(update,update_value)
        mydb.commit() 
        print('your balance account:',deposit)  
    elif input_user == "4":
        # bank.show_balance()
        id_input = input("please enter account number:")
        sql = "SELECT * FROM user WHERE id = %s"
        value = (id_input,)
        mycursor.execute(sql,value)
        myresult = mycursor.fetchall()
        for x in myresult:
            balance = x[4]
        print('your balance account:',balance)    
            
    elif input_user == "5":
        bank.exit_progrram()         
    else:
        print("Invalid choice")  
        input_user = input("Enter your choice : ")  
        
        
         

    


           
        