!pip install ipython-sql
!pip install mysql-connector-python==8.0.27
import pandas as pd
import sqlite3
import  mysql.connector as sql
try:
    conn = sql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        passwd='****', 
        database='bank'
    )
    if conn.is_connected():
        print('Connected successfully')
    conn.close()
except sql.Error as e:
    print(f"Error: {e}")
cur = conn.cursor()
cur.execute(
  'create table customer_details
    (
     acct_no int primary key,
     acct_name varchar(25) ,
     phone_no bigint(25) check(phone_no>11),
     address varchar(25),cr_amt float )'
     )
cur.execute(
  'create table user_table
    (
      username varchar(25) primary key,
      passwrd varchar(25) not null )'
    )
cur.execute(
  'create table transactions
    (
      acct_no int,
      date date,
      withdrawal_amt int,
      amount_added int)'
    )


