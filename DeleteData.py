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

def delete_data_with_condition(dataList, conn):
    sql = ("""DELETE FROM hvh_metrics.table_name
        WHERE hvh_metrics.table_name.column_name IN (%s, %s);
        """)
    try:
        cur = conn.cursor()
        cur.executemany(sql, (dataList,))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.commit()

def delete_data_without_condition(conn):
    commands = ("""
        DELETE FROM hvh_metrics.table_name
        """)
    try:
        cur = conn.cursor()
        cur.execute(commands)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.commit()


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(**params)
        delete_data_with_condition(dataList, conn)
        delete_data_without_condition(conn)

    finally:
        if conn is not None:
            conn.close()
