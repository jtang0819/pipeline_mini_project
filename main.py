import pandas as pd
from sqlalchemy import create_engine


def get_db_connection():
    try:
        connection = create_engine('mysql+pymysql://jordan:jordan@localhost:3306/datapipelineminiproject')
        print("Connection Successful")
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection


def load_third_party(connection, csv_file):
    data = pd.read_csv(csv_file)
    data.to_sql('ticket_sales', con=connection, if_exists='drop', index=False)
    # [Iterate through the CSV file and execute insert statement]
    return


def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "SELECT event_name, sum(num_tickets) as tickets_ordered from ticket_sales group by event_name order by tickets_ordered desc"
    records = pd.read_sql(sql_statement, connection)
    print(records)


# load_third_party(get_db_connection(), "third_party_sales_1.csv")
# import data csv into table
query_popular_tickets(get_db_connection())