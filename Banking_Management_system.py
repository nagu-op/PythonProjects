import random
from tabulate import tabulate
import mysql.connector

def Add_acc():
    while True:
            k=random.randrange(10000,100000)
            nm=input('Enter name : ')
            dob=input('Enter date of birth(yyyy/mm/dd)')
            if len(dob)!=10:
                print('Invalid format')
            adh=input('Enter 12 digit adhaar number : ')
            if len(adh)!=12:
                print('Invalid Aadhaar number')
            mob=input('Enter mobile number : ')
            if len(mob)!=10:
                print('Invalid number')
            gm=input('Enter email id : ')
            bg=input('Enter blood group')
            ch=input('Do you want to deposit initial amount(y/n)')
            if ch in 'Yy':
                bal=int(input('Enter amount to deposite'))
            elif ch in 'Nn':
                bal=0
            
            cur.execute("insert into bank values({},'{}',{})".format(k,nm,bal))
            cur.execute("insert into details values({},'{}','{}','{}','{}','{}','{}')".format(k,nm,dob,adh,mob,gm,bg))
            cur.execute('select * from bank where account_number={}'.format(k))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","Balance_Amount"],tablefmt="pretty")
            print(tbl)
            con.commit()
            chs=input('Do you want to add more account(y/n) : ')
            if chs in 'Nn':
                break



def dep_withd():
    print("""
    
 _________________________________
|          TRANSACTION            |
|                                 |   
|    1.Deposit                    |
|    2.Withdraw                   |     
|    3.Main menu                  |     
 __________________________________
     
    """)
    ch=int(input('Enter choice'))
    a=int(input('Enter account number'))

    while True:
        if ch==1:
            amo=int(input('Enter amount to deposit'))
            cur.execute("select balance_amount from bank where account_number={}".format(a))
            cri=cur.fetchone()
            for i in cri:
                cr=i
            new=cr+amo
            cur.execute("update bank set balance_amount={} where account_number={}".format(new,a))
            print('amount successfully deposited')
            cur.execute("select balance_amount from bank where account_number={}".format(a))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Balance_Amount"],tablefmt="pretty")
            print(tbl)
            con.commit()
            break

        elif ch==2:
            amo=int(input('enter amount to withdraw'))
            cur.execute("select balance_amount from bank where account_number={}".format(a))
            cri=cur.fetchone()
            for i in cri:
                cr=i
            if cr>amo:
                new=cr-amo
                cur.execute("update bank set balance_Amount={} where account_number={}".format(new,a))
                print('amount successfully withdrawn')
                cur.execute("select balance_amount from bank where account_number={}".format(a))
                data=cur.fetchall()
                tbl=tabulate(data,headers=["Balance_Amount"],tablefmt="pretty")
                print(tbl)

                con.commit()
            elif cr<amo:
                print('current balance is insufficient to make withdrawal')
            elif cr==amo:
                p=0
                cur.execute('update bank set balance_amount={} where account_number={}'.format(p,a))
                con.commit()
        if ch==3:
            break


def enq_balance():
    n=int(input("enter the Account number : "))
    cur=con.cursor()
    cur.execute("select account_number,balance_amount from bank where account_number={}".format(n))
    data=cur.fetchall()
    print("""

Your current bank balance is as follows : 

""")
    tbl=tabulate(data,headers=["Balance_Amount"],tablefmt="pretty")
    print(tbl)

def list_acc():

    cur=con.cursor()
    cur.execute("select account_number,name from bank")
    data=cur.fetchall()
    tbl=tabulate(data,headers=["Account_Number","Name"],tablefmt="pretty")
    print(tbl)


def modify_acc():
    n=input("Do you want to display the table first? (Y/N) : ")
    if n in "yY":
        cur.execute("Select * from details")
        data=cur.fetchall()
        tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
        print(tbl)
        
    print()
    accno=int(input("Enter account number : "))####should chage the sentence.....
    print()
    cur.execute("Select * from details where account_number={}".format(accno))
    data=cur.fetchall()
    tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
    print(tbl)
    print("""

 _________________________________________________
|                                                 |
|                  UPDATION                       |   
|    1.Update Name                                |
|    2.Update DOB                                 |     
|    3.Update Aadhar                              |
|    4.Update Mobile number                       |                 
|    5.Update email                               |                              
|    6.Update blood group                         |
|    7.Done                                       |     
 _________________________________________________
 
    """)
    while True:
        choice=int(input("Enter what is to be updated : "))
        if choice==1:
            name=input("Enter new name : ")
            print()
            cur.execute("Update details set name='{}' where account_number={}".format(name,accno))
            cur.execute("Update bank set name='{}' where account_number={}".format(name,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)

        
        elif choice==2:
            dob=input("Enter the new dob: ")
            print()
            cur.execute("Update details set dob='{}' where account_number={}".format(dob,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)
        elif choice==3:
            adhr=input("Enter the aadhar_number : ")
            print()
            cur.execute("Update details set aadhar='{}' where account_number={}".format(adhr,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)
        elif choice==4:
            mob=input("Enter the mobile number : ")
            print()
            cur.execute("Update details set mobile_number='{}' where account_number={}".format(mob,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)
        elif choice==5:
            email=input("Enter the new email id : ")
            print()
            cur.execute("Update details set email='{}' where account_number={}".format(email,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)
        elif choice==6:
            b_g=input("Enter the blood group  : ")
            print()
            cur.execute("Update details set blood_group='{}' where account_number={}".format(b_g,accno))
            con.commit()
            print("Records modified successfully.")
            cur.execute("Select * from details where account_number={}".format(accno))
            data=cur.fetchall()
            tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
            print(tbl)
        elif choice==7:
            print("Exiting...")
            print()
            break
        else:
            print("Invalid choice")
            print()
            continue

def close_acc():
    while True:
        accno=int(input("Enter account number of the  account to be closed : "))
        print()
        sure=input("Are you sure you want to close the account? (Y/N)\n")
        if sure in "yY":
            cur.execute("Delete from bank where account_number={}".format(accno))
            cur.execute("Delete from details where account_number={}".format(accno))
            con.commit()
            print("Account closed successfully.")
            print()
            a=input("Do you want to close more accounts? (Y/N)\n")
            if a in "yY":
                continue
            elif a in "nN":
                break
        elif sure in "nN":
            print("Accont not closed.")
            print()
            break



def display():
    print("The following are the details of all account holders ")
    cur=con.cursor()
    cur.execute("select * from details ")
    data=cur.fetchall()
    tbl=tabulate(data,headers=["Account_Number","Name","dob","aadhar","mobile_number","email","blood_group"],tablefmt="pretty")
    print(tbl)

    print("The following are the bank info")
    cur.execute("select * from bank")
    row=cur.fetchall()
    tbl=tabulate(row,headers=["Account_Number","Name","Balance_Amount"],tablefmt="pretty")
    print(tbl)
ch=int(input("Enter your bank pass_code : "))
if ch==1234:

    
    pass_word = input("Enter your My_Sql password : ")
    
    db=input("Enter the name of the database : ")

    con = mysql.connector.connect(host="localhost", user="root", password=pass_word,database=db)
    if con.is_connected():
        print("You have successfully logged in.....")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS details (Account_Number int,Name varchar(40),dob varchar(10),aadhar varchar(12),mobile_number varchar(10),email varchar(50),blood_group varchar(3))")
    cur.execute("CREATE TABLE IF NOT EXISTS bank (Account_Number int,Name varchar(40),balance_amount int)")
    con.commit()
else:
    print("Invalid passcode..")



while True:

    
    print("""


 _________________________________________________
|                                                 |
|                  MENU                           |
|                                                 |    
|    1.TO ADD A NEW BANK ACCOUNT.                 |
|                                                 |
|    2.To DEPOSIT OR WITHDRAW.                    |     
|                                                 |
|    3.To ENQUIRE BALANCE AMOUNT.                 |
|                                                 |
|    4.To SHOW COMPLETE DETAILS OF ALL ACCOUNTS.  |                 
|                                                 |
|    5.TO VIEW LIST OF ALL ACCOUNT HOLDERS.       |                     
|                                                 |
|    6.TO MODIFY AN ACCOUNT.                      |
|                                                 |
|    7.TO CLOSE AN ACCOUNT.                       |
|                                                 |  
|    0.TO EXIT THE PROGRAM.                       |    
|                                                 |      
 _________________________________________________
 """)
    ch=int(input("Enter Your choice : "))
    if ch==1:
        Add_acc()
    elif ch==2:
        dep_withd()
    elif ch==3:
        enq_balance()
    elif ch==4:
        display()
    elif ch==5:
        list_acc()
    elif ch==6:
        modify_acc()
    elif ch==7:
        close_acc()
    elif ch==0:
        print("Thank you for using the program.....")
        break
cur.close()
con.close()
