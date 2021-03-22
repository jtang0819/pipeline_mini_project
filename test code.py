import pandas as pd
import mysql.connector
import pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://jordan:jordan@localhost:3306/datapipelineminiproject')
# connection = mysql.connector.connect(user='jordan',
#                                      password='jordan',
#                                      host='localhost',
#                                      port='3306',
#                                      database='datapipelineminiproject')


# x = connection.cursor()
# x.execute(
#     '''create table dummy (
# ticket_id INT,
# trans_date INT,
# event_id INT,
# event_name VARCHAR(50),
# event_date DATE,
# event_type VARCHAR(10),
# event_city VARCHAR(20),
# event_addr VARCHAR(100),
# customer_id INT,
# price DECIMAL,
# num_tickets INT
#     )'''
# )
# x.close()
data = pd.read_csv("third_party_sales_1.csv")
data.to_sql('dummy', con=engine, if_exists='append', index=False)
