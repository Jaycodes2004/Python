import matplotlib.pyplot as plt
import mysql.connector as con
import random as rm
import pandas as pd
import numpy as np
from faker import Faker
from datetime import date
fake=Faker()
c_df=[]
o_df=[]
# connecting MySql
def mysqlcon():
    global db,runcmd
    db = con.connect(host='localhost',user='root',passwd='1234')
    runcmd = db.cursor()
    runcmd.execute("CREATE DATABASE IF NOT EXISTS Orders")
    runcmd.execute("USE Orders;")
    if (db):
        print("Connection Successful")
        print("Using database : \"Orders\"")
    else:
        print("Error , Connection Unsuccessful ")

# creating table :-
def Table_cr():
    #creating Customer Table
    Customer_tab = '''CREATE TABLE IF NOT EXISTS  `customer` (
      `CustomerID` INT ,
      `First_name` VARCHAR(200) NOT NULL,
      `Last_name` VARCHAR(200) NOT NULL,
      `Email` VARCHAR(300) NOT NULL,
      `Address` VARCHAR(500) NOT NULL,
      `City` VARCHAR(60) NOT NULL,
      `State` VARCHAR(50) NOT NULL,
      `Country` VARCHAR(50) NOT NULL,
      `Postal_code` MEDIUMINT(10) NOT NULL,
      PRIMARY KEY (`CustomerID`),
      UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE); '''  

    # creating order table
    order_tab = '''CREATE TABLE IF NOT EXISTS `order` (
      `Order_Id` INT ,
      `Customer_Id` INT NOT NULL,
      `Date` DATETIME(6) NOT NULL,
      `Amt` DECIMAL NOT NULL,
      `Ship_Address` VARCHAR(500) NOT NULL,
      `Ship_City` VARCHAR(60) NOT NULL,
      `Ship_State` VARCHAR(50) NOT NULL,
      `Ship_Country` VARCHAR(100) NOT NULL,
      `Postal_code` MEDIUMINT(10) NOT NULL,
      PRIMARY KEY (`Order_Id`),
      UNIQUE INDEX `Customer_Id_UNIQUE` (`Customer_Id` ASC) VISIBLE,
      CONSTRAINT `Customer_Id`
        FOREIGN KEY (`Customer_Id`)
        REFERENCES `orders`.`customer` (`CustomerID`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION);'''
    runcmd.execute(Customer_tab)
    runcmd.execute(order_tab)
    print("Customer and order table is created")

def date():
    import datetime
    import random
    from datetime import timedelta
    d = datetime.date.today() - timedelta(days=7)
    today = datetime.date.today()
    random_date = random.randint(d.toordinal(), today.toordinal())
    random_date = datetime.date.fromordinal(random_date)
    return random_date

# creating sample data of customer & order table
def data():
    for i in range(num-1):
        a=0
        s=[]
        d=[]
        f_name=fake.first_name()
        l_name=fake.last_name()
        cus_id=rm.randint(100000,999999)
        order_id=rm.randint(100000,999999)
        e_no=rm.randint(100,999) # email number
        emailid=f_name+l_name+str(e_no)+"@gmail.com"
        address=fake.address()
        state=fake.state()
        city=fake.city()
        country=fake.country()
        order_date=date()
        postal_code=fake.postcode()
        amt=round(r.uniform(500.0,10000.99),2)
        s.extend([cus_id,f_name,l_name,email,address,city,state,country,postal_code])
        d.extend([order_id,order_date,amt,address,city,state,country,postal_code])
        c_df.append(s)
        o_df.append(d)
        
    

def main():
    mysqlcon()
    Table_cr()
    num=100
    s_form(num)
    dft = pd.DataFrame(df,columns=list1)
    dft.set_index("Customer_id", inplace = True)
    print(dft)
    dft.to_csv('C:\stud.csv')
data()
