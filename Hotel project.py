print("********WELCOME TO RR HOTEL********")
print("Food categories")
print("1.Vegetarion")
print("2.non-Vegatarion")
import datetime
x=datetime.datetime.now()
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="4321",
    database="food_bill_db"
)
mycusor=mydb.cursor()
#mycusor.execute("create database Food_Bill_db")
#mycusor.execute("create table Veg_Bill (Date_time varchar(255),Orders varchar(255),Order_count varchar(255),Total_Bill varchar(255))")
#mycusor.execute("create table Non_Veg_Bill (Date_time varchar(255),Orders varchar(255),Order_count varchar(255),Total_Bill varchar(255))")
def meal1():
    veg_menu=["ven pongal","pongal","idly","poori","dosa","masal dosa","rava upma",
              "mushroom biryani","lemon rice","fried rice","veg biryani","curd rice"]
    myiter=iter(veg_menu)
    print("Your veg menu:")
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    order=input("\nEnter your order:").lower()
    idly=10
    ven_pongal=50
    poori=15
    masal_dosa=30
    rava_upma=40
    mushroom_biryani=70
    lemon_rice=30
    dosa=20
    pongal=35
    fried_rice=35
    veg_biryani=60
    curd_rice=35
    if order in veg_menu:
        print(f"Yes your {order} is available")
        how_many=int(input("How many you want:"))
        if order=="idly":
            total=idly*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="ven pongal":
            total=ven_pongal*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="poori":
            total=poori*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="pongal":
            total=pongal*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="masal dosa":
            total=masal_dosa*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="rava upma":
            total=rava_upma*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="lemon rice":
            total=lemon_rice*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="dosa":
            total=dosa*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="mushroom biryani":
            total=mushroom_biryani*how_many
            print("\n")
            print("------------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("------------------------------------------")
        elif order=="fried rice":
            total=fried_rice*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="veg biryani":
            total=veg_biryani*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="curd rice": 
            total=curd_rice*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        else:
            print(f"Please choose the order in the Menu")
        sql="insert into Veg_Bill (Date_time,Orders,Order_count,Total_Bill) values (%s,%s,%s,%s)"
        val=(x,order,how_many,f"{total} Rs")
        mycusor.execute(sql,val)
        mydb.commit()
        
def meal2():
    non_veg_menu=["chicken biryani","mutton biryani","fish fry","egg rice","chicken rice",
              "egg noodles","mutton soup","chicken 65"]
    myiter=iter(non_veg_menu)
    print("Your Non-veg menu:")
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    order=input("Enter your order:").lower()
    chicken_biryani=80
    mutton_biryani=100
    egg_rice=60
    fish_fry=30
    chicken_rice=70
    egg_noodles=70
    mutton_soup=50
    chiken_65=60
    if order in non_veg_menu:
        print(f"Yes your {order} is available")
        how_many=int(input("How many you want:"))
        if order=="chicken biryani":
            total=chicken_biryani*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="mutton biryani":
            total=mutton_biryani*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="egg rice":
            total=egg_rice*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="fish fry":
            total=fish_fry*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="chicken rice":
            total=chicken_rice*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="egg noodles":
            total=egg_noodles*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="mutton soup":
            total= mutton_soup*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        elif order=="chicken 65":
            total=chiken_65*how_many
            print("\n")
            print("----------------------------------------")
            print(x)
            print(f"Your bill for {how_many} {order} is Rs.{total}")
            print("----------------------------------------")
        else:
            print(f"Please choose the order in the Menu")
        sql="insert into Non_Veg_Bill (Date_time,Orders,Order_count,Total_Bill) values (%s,%s,%s,%s)"
        val=(x,order,how_many,f"{total} Rs")
        mycusor.execute(sql,val)
        mydb.commit()

meal_type=int(input("Enter your Number:"))
if meal_type==1:
    meal1() 
elif meal_type==2:
    meal2()
else:
    print("Use only number either 1 or2")