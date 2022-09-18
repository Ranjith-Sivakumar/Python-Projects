import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="4321",
    database="ATM_data_db"
    )
mycursor=mydb.cursor()
#mycursor.execute("Create database ATM_data_db")
#mycursor.execute("create table ATM_data (Account_No varchar(255),Date_time varchar(255),First_Balance varchar(255),debited_Amount varchar(255),Amount_deposited varchar(255),Current_Balance varchar(255))")
#print("Done")

import datetime
Ac_No=67542348654327
D=datetime.datetime.now()
print("Welcome to ATM")
print("Please insert Your card")
password=2354
U_pin=int(input("Enter your pin:"))
balance=10000
if U_pin==password:
    print("Please choose one from the following options")
    print("1. Show Balance")
    print("2. Withdraw Amount")
    print("3. Deposite Amount")
    print("4. Exit")
    option=int(input("Enter your Option:"))
    if option==1:
        print(f"Your current balance is {balance}")
        sql="insert into ATM_data (Account_No ,Date_time ,First_Balance ,debited_Amount ,Amount_deposited,Current_Balance ) values (%s,%s,%s,%s,%s,%s)"
        val=(Ac_No,D,f"{balance} Rs checked","Nil","Nil",f"{balance} Rs")
        mycursor.execute(sql,val)
        mydb.commit()
    elif option==2:
        try:
            amount=int(input("Please enter the amount:"))
            if amount!=balance:
                D_balance=balance-amount
                pin=int(input("Please Re-enter the pin again:"))
                if pin==password:
                    print(f"Your withdraw amount {amount} Rs is debited from your account")
                    print(f"Your current balance is {D_balance} Rs")
                    sql="insert into ATM_data (Account_No ,Date_time ,First_Balance ,debited_Amount ,Amount_deposited,Current_Balance) values (%s,%s,%s,%s,%s,%s)"
                    val=(Ac_No,D,f"{balance} Rs",f"{amount} Rs","Nil",f"{D_balance} Rs")
                    mycursor.execute(sql,val)
                    mydb.commit()
                else:
                    print("Wrong pin check your pin or try again Later")
            else:
                print("Please enter the valied amount")
        except:
            print("Use only numbers")
    elif option==3:
        D_amount=int(input("Please enter the deposite amount:"))
        D_balance=balance+D_amount
        pin=int(input("Please Re-enter the pin again:"))
        if pin==password:
            print(f"Your deposite amount {D_amount} Rs is credited to your account")
            print(f"Your current balance is {D_balance} Rs")
            sql="insert into ATM_data (Account_No ,Date_time ,First_Balance ,debited_Amount ,Amount_deposited,Current_Balance ) values (%s,%s,%s,%s,%s,%s)"
            val=(Ac_No,D,f"{balance} Rs","Nil",f"{D_amount}",f"{D_balance} Rs")
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            print("Wrong pin check your pin or try again Later")
    elif option==4:
        print()
    else:
        print("Please choose the valied option")
    
else:
    print("Re-check your pin")
