# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Sameer Ansari)s
"""
import mysql.connector
from mysql.connector import Error
try:
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root1234',
        database='Bank',
        auth_plugin='mysql_native_password')

    print(mydb)

except Error as e:
    print("Error is : ",e)
    
mycursor=mydb.cursor(buffered=True)
#mycursor.execute('create database Bank')

def Menu():
    print("-"*50,"NON-TRANSACTIONAL RECORD DATABASE","-"*50)
    print("-"*140)
    print("MAIN MENU".center(140))
    print("1. Display Records ".center(140))
    print("2. Insert Record ".center(140))
    print("3. Search Record by Acc No. ".center(140))
    print("4. Update Record ".center(140))
    print("5. Delete Record ".center(140))
    print("6. Exit ".center(140))
    print("-"*140)

def Create():
    try:
        mycursor.execute('create table account(AccNo varchar(8),Name varchar(20),ContactNo varchar(12),CityPinCode varchar(8),Bal varchar(8)')
        print("Table Created")        
    except:
        print("Table Already Exists")
    mydb.commit()

def Insert():
    while True:
        AccNo=input("Enter Account Number: ")
        Name=input("Enter Name: ")
        ContactNo=input("Enter Contact number: ")
        CityPinCode=input("Enter City Pin Code: ")
        Bal=input("Enter Balance Amount: ")
        Rec=[AccNo,Name,ContactNo,CityPinCode,Bal]
        cmd='insert into account values(%s,%s,%s,%s,%s)'
        mycursor.execute(cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more RECORDS Y/N: ")
        if ch=='N':
            break
        
def display():
    try:
        cmd='select * from account order by AccNo';
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s'
        print(F%("AccNo","Name","ContactNo","CityPinCode","Bal"))
        print("*"*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
                print()
        print("-"*125)
    except:
        print("Table Doesn't Exist")

def Search():
     try:
         cmd='select * from account'
         mycursor.execute(cmd)
         ch=input("Enter Acc no. to be searched : ")
         for i in mycursor:
             if i[0]==ch:
                 print("-"*125)
                 F='%15s %15s %15s %15s %15s'
                 print(F%("AccNo","Name","ContactNo","CityPinCode","Bal"))
                 print("*"*125)
                 for j in i:
                     print("%14s" % j, end=' ')
                     print()
                     break
             else:
                 print("Record not found, enter valid Acc No. ")
     except:
        print("Table doesn't Exist.")   

def Update():
    try:
         cmd='select * from account'
         mycursor.execute(cmd)
         A=input("Enter Acc No. whose detail to be updated : ")
         for i in mycursor:
             if i[0]==A:
                 ch=input("Change Name[Y/N]: ")
                 if ch=='Y':
                     i[1]=input("Enter Name : ")
                 ch=input("Change Contact Info[Y/N]: ")
                 if ch=='Y':
                     i[1]=input("Enter Contact Info : ")     
                 ch=input("Change CityPinCode[Y/N]: ")
                 if ch=='Y':
                     i[1]=input("Enter CityPinCode : ")
                 ch=input("Change Balance[Y/N]: ")
                 if ch=='Y':
                     i[1]=float(input("Enter Balance : "))
                 cmd='update account set Name=%s,ContactNo=%s,ContactNo=%s,ContactNo=%s where AccNo=%s'
                 val=(i[1],i[2],i[3],i[4],i[0])
                 mycursor.execute(cmd,val)
                 mydb.commit()
                 print("Account updated")
                 break
         else:
             print("Account not found")

    except:
        print("Table doesn't exist")
        
def Delete():
    try:
         cmd='select * from account'
         mycursor.execute(cmd)
         A=input("Enter Acc No. whose detail to be Deleted: ")
         for i in mycursor:
             i=list(i)
             if i[0]==A:
                 cmd='delete from table where AccNo=%s'
                 val=(i[0],)
                 mycursor.execute(cmd,val)
                 mydb.commit()
                 print("Account Deleted ")
                 break
         else:
             print("Record not found")    
    except:
        print("Table doesn't exist")

while True:
    Menu()
    ch=input("Enter your choice : ")
    if ch=='0':
        Create()
    elif ch=='1':
        display()
    elif ch=='2':
        Insert()
    elif ch=='3':
        Search()
    elif ch=='4':
        Update()
    elif ch=='5':
        Delete()
    elif ch=='6':
        exit()    
    else:
        print("Invalid Choice: Enter choice according to MENU.")                