print("Welcome to ABC Ticket Booking Site")
print("1.Movie Ticket Booking")
print("2.Train Ticket Booking")
import random
from re import S
import string
import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="4321",
    database="Ticket_booking_db"
)
mycusor=mydb.cursor()
#mycusor.execute("Create database Ticket_booking_db")
#mycusor.execute("Create Table Movie_Ticket (Booked_Time varchar(255),Theater_Name varchar(255),Ticket_ID varchar(255),Row_No varchar(255),Seat_count varchar (255),Show_Date varchar(255),Show_Time varchar(255),Total_Bill varchar(255))")
#mycusor.execute("Create Table Train_Ticket (Booked_Time varchar(255),Ticket_ID varchar(255),Name varchar(255),Traveling_Place varchar(255),Travel_Date varchar(255),Travel_Timing varchar(255),Travel_Mode varchar(255),Amount_Paid varchar(255))")
D_time=datetime.datetime.now()
user=int(input("Enter your Number:"))

def Movie():
    Theater_Names=["1.Bala Muragan","2.CKC","3.Kalai Magal","4.Senthil Kumaran"]
    print("Theaters available in your Location")
    for i in Theater_Names:
        print(i)
    x=int(input("Enter your Option:"))
    if x==1:
        print("Welcome to Bala Muragan Theater")
        print("Total rows 40")
        print("Each row have 10 Seats")
        seat=150
        print(f"Each seat is {seat} Rs")
        row=int(input("Enter your row No:"))
        if row<=40:
            How_many=int(input("How many seat you want:"))
            date=input("Enter the Movie date:")
            Morning_show="9:30-12:30"
            After_Show="2:00-5:00"
            Evening_show="6:30-9:30"
            Night_show="11:00-2:00"
            print(f"Show timing\nMorning show:{Morning_show}\nAfternoon show:{After_Show}\nEvening show:{Evening_show}\nNight show:{Night_show}")
            time=input("Enter your show time:").lower()
            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
            print(date)
            print("---------------------------------------")
            print(f"Your ticket id is {ticket_id}")
            try:
                if time==Morning_show or time=="morning show":
                    print(f"Booked Date is{date}\nBooked time is {Morning_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==After_Show or time=="afternoon show":
                    print(f"Booked Date is{date}\nBooked time is {After_Show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Evening_show or time=="evening show":
                    print(f"Booked Date is{date}\nBooked time is {Evening_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Night_show or time=="night show":
                    print(f"Booked Date is{date}\nBooked time is {Night_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                else:
                    print("You choose Wrong Time")
                sql="insert into Movie_Ticket(Booked_Time,Theater_Name,Ticket_ID,Row_No,Seat_count,Show_Date,Show_Time,Total_Bill ) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(D_time,"Bala Muragan",ticket_id,row,How_many,date,time,f"{bill} Rs")
                mycusor.execute(sql,val)
                mydb.commit()
            except:
                print("Please choose correct Time")
              
        else:
            print(f"Choose Between {row} rows")
    elif user==2:
        print("Welcome to CKC Theater")
        print("Total rows 45")
        print("Each row have 10 Seats")
        seat=180
        print(f"Each seat is {seat} Rs")
        row=int(input("Enter your row No:"))
        if row<=45:
            How_many=int(input("How many seat you want:"))
            date=input("Enter the Movie date:")
            Morning_show="9:00-12:00"
            After_Show="2:00-5:00"
            Evening_show="7:00-10:00"
            Night_show="11:30-2:30"
            print(f"Show timing\nMorning show:{Morning_show}\nAfternoon show:{After_Show}\nEvening show:{Evening_show}\nNight show:{Night_show}")
            time=input("Enter your show time:").lower()
            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
            print(date)
            print("---------------------------------------")
            print(f"Your ticket id is {ticket_id}")
            try:
                if time==Morning_show or time=="morning show":
                    print(f"Booked Date is{date}\nBooked time is {Morning_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==After_Show or time=="afternoon show":
                    print(f"Booked Date is{date}\nBooked time is {After_Show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Evening_show or time=="evening show":
                    print(f"Booked Date is{date}\nBooked time is {Evening_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Night_show or time=="night show":
                    print(f"Booked Date is{date}\nBooked time is {Night_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                else:
                    print("You choose Wrong Time")
                sql="insert into Movie_Ticket(Booked_Time,Theater_Name,Ticket_ID,Row_No,Seat_count,Show_Date,Show_Time,Total_Bill ) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(D_time,"CKC",ticket_id,row,How_many,date,time,f"{bill} Rs")
                mycusor.execute(sql,val)
                mydb.commit()
            except:
                print("Please choose correct Time")
        else:
            print(f"Choose Between {row} rows")
    elif user==3:
        print("Welcome to Kalai Magal Theater")
        print("Total rows 40")
        print("Each row have 10 Seats")
        seat=130
        print(f"Each seat is {seat} Rs")
        row=int(input("Enter your row No:"))
        if row<=40:
            How_many=int(input("How many seat you want:"))
            date=input("Enter the Movie date:")
            Morning_show="10:00-1:00"
            After_Show="3:00-6:00"
            Evening_show="8-11:00"
            print(f"Show timing\nMorning show:{Morning_show}\nAfternoon show:{After_Show}\nEvening show:{Evening_show}\nNight show:{Night_show}")
            time=input("Enter your show time:").lower()
            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
            print(date)
            print("---------------------------------------")
            print(f"Your ticket id is {ticket_id}")
            try:
                if time==Morning_show or time=="morning show":
                    print(f"Booked Date is{date}\nBooked time is {Morning_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==After_Show or time=="afternoon show":
                    print(f"Booked Date is{date}\nBooked time is {After_Show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Evening_show or time=="evening show":
                    print(f"Booked Date is{date}\nBooked time is {Evening_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Night_show or time=="night show":
                    print(f"Booked Date is{date}\nBooked time is {Night_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                else:
                    print("You choose Wrong Time")
                sql="insert into Movie_Ticket(Booked_Time,Theater_Name,Ticket_ID,Row_No,Seat_count,Show_Date,Show_Time,Total_Bill ) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(D_time,"Kalai Magal",ticket_id,row,How_many,date,time,f"{bill} Rs")
                mycusor.execute(sql,val)
                mydb.commit()
            except:
                print("Please choose correct Time")
        else:
            print(f"Choose Between {row} rows")
    elif user==4:
        print("Welcome to Senthil Kumaran Theater")
        print("Total rows 40")
        print("Each row have 10 Seats")
        seat=190
        print(f"Each seat is {seat} Rs")
        row=int(input("Enter your row No:"))
        if row<=40:
            How_many=int(input("How many seat you want:"))
            date=input("Enter the Movie date:")
            Morning_show="9:30-12:30"
            After_Show="2:00-5:00"
            Evening_show="6:30-9:30"
            Night_show="11:00-2:00"
            print(f"Show timing\nMorning show:{Morning_show}\nAfternoon show:{After_Show}\nEvening show:{Evening_show}\nNight show:{Night_show}")
            time=input("Enter your show time:").lower()
            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
            print(date)
            print("---------------------------------------")
            print(f"Your ticket id is {ticket_id}")
            try:
                if time==Morning_show or time=="morning show":
                    print(f"Booked Date is{date}\nBooked time is {Morning_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==After_Show or time=="afternoon show":
                    print(f"Booked Date is{date}\nBooked time is {After_Show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Evening_show or time=="evening show":
                    print(f"Booked Date is{date}\nBooked time is {Evening_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                elif time==Night_show or time=="night show":
                    print(f"Booked Date is{date}\nBooked time is {Night_show}")
                    print(f"Your booked on {row} and {How_many} Seats")
                    bill=seat*How_many
                    print(f"Your total Bill is {bill} Rs")  
                    print("---------------------------------------")
                else:
                    print("You choose Wrong Time")
                sql="insert into Movie_Ticket(Booked_Time,Theater_Name,Ticket_ID,Row_No,Seat_count,Show_Date,Show_Time,Total_Bill ) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(D_time,"Senthil Kumaran",ticket_id,row,How_many,date,time,f"{bill} Rs")
                mycusor.execute(sql,val)
                mydb.commit()
            except:
                print("Please choose correct Time")
        else:
            print(f"Choose Between {row} rows") 
            
              
def Train():
    Place=["tirupattur","chennai","coimbatore","banglore"]
    s=input("From:").lower()
    e=input("To:").lower()
    date=input(f"Enter the date:")
    Ac=input("Ac or Non Ac:").upper()
    if s in Place and e in Place:
            if s=="tirupattur" or s=="chennai" and e=="chennai" or e=="tirupattur":
                A_time=["Morning Timing:","2:00 AM","4:00 AM","7:00 AM","Afternoon Timing:","12:00 PM","3:00 PM","Evening Timing","4:00 PM","7:00 PM"]
                myiter=iter(A_time)
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
                time=input("Enter your time:").upper()
                if Ac=="AC":
                        amount=500
                        print(f"Your total amount for the travel is {amount} Rs.")
                        Ticket_status=input("Can I confirming the ticket:").lower()
                        if Ticket_status=="yes":
                            Name=input("Enter your Name:").upper()
                            how_many=int(input("How many Ticket You want:"))
                            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                            total=amount*how_many
                            print("---------------------------------------")
                            print(f"Ticket ID        : {ticket_id}")
                            print(f"Location         :{s} to {e}")
                            print(f"Name             : {Name}")
                            print(f"Date             : {date}")
                            print(f"Time             : {time}")
                            print(f"Total Amount paid: {total} Rs,{Ac} Coach")
                            print("---------------------------------------")
                            sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,Ac,f"{total} Rs")
                            mycusor.execute(sql,val)
                            mydb.commit()
                        else:
                            print("Please write only Yes or No")
                elif Ac=="NON AC":
                        sleeper=input("Sleeper or Second Class:").lower()
                        if sleeper=="sleeper":
                            S_amount=150
                            print(f"Your total amount for the travel is {S_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=S_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper} Coach")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                            else:
                                print("Please write only Yes or No")
                        elif sleeper=="second class":
                            Sc_amount=100
                            print(f"Your total amount for the travel is {Sc_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=Sc_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper}")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                                
                            else:
                             print("Please write only Yes or No")
                        else:
                            print("Please Choose correct Option")
                else:
                    print("Please Choose Ac or Non Ac only")
            elif s=="banglore" or s=="chennai" and e=="chennai" or e=="banglore":
                A_time=["Morning Timing:","2:00 AM","4:00 AM","7:00 AM","Afternoon Timing:","12:00 PM","3:00 PM","Evening Timing","4:00 PM","7:00 PM"]
                myiter=iter(A_time)
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
                time=input("Enter your time:").upper()
                if Ac=="AC":
                        amount=1200
                        print(f"Your total amount for the travel is {amount} Rs.")
                        Ticket_status=input("Can I confirming the ticket:").lower()
                        if Ticket_status=="yes":
                            Name=input("Enter your Name:").upper()
                            how_many=int(input("How many Ticket You want:"))
                            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                            total=amount*how_many
                            print("---------------------------------------")
                            print(f"Ticket ID        : {ticket_id}")
                            print(f"Location         :{s} to {e}")
                            print(f"Name             : {Name}")
                            print(f"Date             : {date}")
                            print(f"Time             : {time}")
                            print(f"Total Amount paid: {total} Rs,{Ac} Coach")
                            print("---------------------------------------")
                            sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,Ac,f"{total} Rs")
                            mycusor.execute(sql,val)
                            mydb.commit()
                        else:
                            print("Please write only Yes or No")
                elif Ac=="NON AC":
                        sleeper=input("Sleeper or Second Class:").lower()
                        if sleeper=="sleeper":
                            S_amount=650
                            print(f"Your total amount for the travel is {S_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=S_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper} Coach")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                            else:
                                print("Please write only Yes or No")
                        elif sleeper=="second class":
                            Sc_amount=250
                            print(f"Your total amount for the travel is {Sc_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=Sc_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper}")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                                
                            else:
                             print("Please write only Yes or No")
                        else:
                            print("Please Choose correct Option")
                else:
                    print("Please Choose Ac or Non Ac only")
            elif s=="tirupattur" or s=="coimbatore" and e=="coimbatore" or e=="tirupattur":
                A_time=["Morning Timing:","2:00 AM","4:00 AM","7:00 AM","Afternoon Timing:","12:00 PM","3:00 PM","Evening Timing","4:00 PM","7:00 PM"]
                myiter=iter(A_time)
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
                time=input("Enter your time:").upper()
                if Ac=="AC":
                        amount=500
                        print(f"Your total amount for the travel is {amount} Rs.")
                        Ticket_status=input("Can I confirming the ticket:").lower()
                        if Ticket_status=="yes":
                            Name=input("Enter your Name:").upper()
                            how_many=int(input("How many Ticket You want:"))
                            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                            total=amount*how_many
                            print("---------------------------------------")
                            print(f"Ticket ID        : {ticket_id}")
                            print(f"Location         :{s} to {e}")
                            print(f"Name             : {Name}")
                            print(f"Date             : {date}")
                            print(f"Time             : {time}")
                            print(f"Total Amount paid: {total} Rs,{Ac} Coach")
                            print("---------------------------------------")
                            sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,Ac,f"{total} Rs")
                            mycusor.execute(sql,val)
                            mydb.commit()
                        else:
                            print("Please write only Yes or No")
                elif Ac=="NON AC":
                        sleeper=input("Sleeper or Second Class:").lower()
                        if sleeper=="sleeper":
                            S_amount=150
                            print(f"Your total amount for the travel is {S_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=S_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper} Coach")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                            else:
                                print("Please write only Yes or No")
                        elif sleeper=="second class":
                            Sc_amount=100
                            print(f"Your total amount for the travel is {Sc_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=Sc_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper}")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                                
                            else:
                             print("Please write only Yes or No")
                        else:
                            print("Please Choose correct Option")
                else:
                    print("Please Choose Ac or Non Ac only")
            elif s=="tirupattur" or s=="banglore" and e=="banglore" or e=="tirupattur":
                A_time=["Morning Timing:","2:00 AM","4:00 AM","7:00 AM","Afternoon Timing:","12:00 PM","3:00 PM","Evening Timing","4:00 PM","7:00 PM"]
                myiter=iter(A_time)
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
                time=input("Enter your time:").upper()
                if Ac=="AC":
                        amount=800
                        print(f"Your total amount for the travel is {amount} Rs.")
                        Ticket_status=input("Can I confirming the ticket:").lower()
                        if Ticket_status=="yes":
                            Name=input("Enter your Name:").upper()
                            how_many=int(input("How many Ticket You want:"))
                            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                            total=amount*how_many
                            print("---------------------------------------")
                            print(f"Ticket ID        : {ticket_id}")
                            print(f"Location         :{s} to {e}")
                            print(f"Name             : {Name}")
                            print(f"Date             : {date}")
                            print(f"Time             : {time}")
                            print(f"Total Amount paid: {total} Rs,{Ac} Coach")
                            print("---------------------------------------")
                            sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,Ac,f"{total} Rs")
                            mycusor.execute(sql,val)
                            mydb.commit()
                        else:
                            print("Please write only Yes or No")
                elif Ac=="NON AC":
                        sleeper=input("Sleeper or Second Class:").lower()
                        if sleeper=="sleeper":
                            S_amount=400
                            print(f"Your total amount for the travel is {S_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=S_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper} Coach")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                            else:
                                print("Please write only Yes or No")
                        elif sleeper=="second class":
                            Sc_amount=200
                            print(f"Your total amount for the travel is {Sc_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=Sc_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper}")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                                
                            else:
                             print("Please write only Yes or No")
                        else:
                            print("Please Choose correct Option")
                else:
                    print("Please Choose Ac or Non Ac only")
            elif s=="tirupattur" or s=="coimbatore" and e=="coimbatore" or e=="tirupattur":
                A_time=["Morning Timing:","2:00 AM","4:00 AM","8:00 AM","Afternoon Timing:","12:00 PM","3:00 PM","Evening Timing","4:00 PM","7:00 PM"]
                myiter=iter(A_time)
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
                time=input("Enter your time:").upper()
                if Ac=="AC":
                        amount=500
                        print(f"Your total amount for the travel is {amount} Rs.")
                        Ticket_status=input("Can I confirming the ticket:").lower()
                        if Ticket_status=="yes":
                            Name=input("Enter your Name:").upper()
                            how_many=int(input("How many Ticket You want:"))
                            ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                            total=amount*how_many
                            print("---------------------------------------")
                            print(f"Ticket ID        : {ticket_id}")
                            print(f"Location         :{s} to {e}")
                            print(f"Name             : {Name}")
                            print(f"Date             : {date}")
                            print(f"Time             : {time}")
                            print(f"Total Amount paid: {total} Rs,{Ac} Coach")
                            print("---------------------------------------")
                            sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,Ac,f"{total} Rs")
                            mycusor.execute(sql,val)
                            mydb.commit()
                        else:
                            print("Please write only Yes or No")
                elif Ac=="NON AC":
                        sleeper=input("Sleeper or Second Class:").lower()
                        if sleeper=="sleeper":
                            S_amount=150
                            print(f"Your total amount for the travel is {S_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=S_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper} Coach")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                            else:
                                print("Please write only Yes or No")
                        elif sleeper=="second class":
                            Sc_amount=100
                            print(f"Your total amount for the travel is {Sc_amount} Rs.")
                            Ticket_status=input("Can I confirming the ticket:").lower()
                            if Ticket_status=="yes":
                                Name=input("Enter your Name:").upper()
                                how_many=int(input("How many Ticket You want:"))
                                ticket_id="".join(random.choices(string.ascii_uppercase+string.digits,k=10))
                                total=Sc_amount*how_many
                                print("---------------------------------------")
                                print(f"Ticket ID        : {ticket_id}")
                                print(f"Location         :{s} to {e}")
                                print(f"Name             : {Name}")
                                print(f"Date             : {date}")
                                print(f"Time             : {time}")
                                print(f"Total Amount paid: {total} Rs,{sleeper}")
                                print("---------------------------------------")
                                sql="Insert into Train_Ticket (Booked_Time,Ticket_ID,Name,Traveling_Place,Travel_Date,Travel_Timing,Travel_Mode,Amount_Paid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(D_time,ticket_id,Name,f"{e} to {s}",date,time,f"{Ac} {sleeper}",f"{total} Rs")
                                mycusor.execute(sql,val)
                                mydb.commit()
                                
                            else:
                             print("Please write only Yes or No")
                        else:
                            print("Please Choose correct Option")
                else:
                    print("Please Choose Ac or Non Ac only")
            else:
                print()
    else:
        print(f"sorry sir your travel form {s} to {e} is not available ")
if user==1:
    Movie()
elif user==2:
    Train()
