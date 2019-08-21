import psycopg2
import os
import sys
import warnings
from psycopg2 import extras
warnings.filterwarnings("ignore")

params = {'host': 'server',
          'database': 'database_name',
          'user': 'user_name',
          'password': 'password'}


def get_data(conn):
    command = ("""
        SELECT * FROM hvh_metrics.table_name
        """)
    try:
        cur = conn.cursor()
        df = pandas.read_sql(command, con=conn)
        return df
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()



if __name__ == '__main__':
    try:
        conn = psycopg2.connect(**params)
        df=get_data(conn)

    finally:
        if conn is not None:
            conn.close()
