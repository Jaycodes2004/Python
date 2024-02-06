import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as con
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
mysqlcon()
