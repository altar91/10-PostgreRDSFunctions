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

def bulk_insert(dataframe, tblName, conn):
    try:
        table_columns = ""
        j = 1
        for i in dataframe.columns:
            if j == 1:
                table_columns = i
                j = 0
            else:
                table_columns = table_columns + ", " + i

        values = [tuple(x) for x in dataframe.values]
        schema_name = 'hvh_metrics'
        table_name = tblName
        columns = table_columns

        number_of_values = '(%s' + (len(values[0]) - 1) * ',%s' + ')'
        cur = conn.cursor()
        psycopg2.extras.execute_batch(cur,
                                      """INSERT INTO {t} ({c}) VALUES {v};""".format(
                                          t=schema_name + '.' + table_name, c=columns, v=number_of_values), values, page_size=500)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.commit()

def insert_data_on_conflict(dataList, conn):
    sql = ("""
        INSERT INTO hvh_metrics.table_name(column1, column1 ..) Values (%s, %s, ..)
        ON CONFLICT (KEY)
        DO update set Value_column= EXCLUDED.Value_column, Value_column2= EXCLUDED.Value_column2;
        """)

    try:
        cur = conn.cursor()
        cur.executemany(sql, dataList)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.commit()


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(**params)
        insert_data_on_conflict(dataframe_name.values.tolist(), conn)
        bulk_insert(dfAPP, "table_name", conn)

    finally:
        if conn is not None:
            conn.close()
