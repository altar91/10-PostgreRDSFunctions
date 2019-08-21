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

def create_table(conn):
    commands = (
        """
        CREATE TABLE hvh_metrics.table_name (
            table_name_id SERIAL PRIMARY KEY,
            Char_Column VARCHAR(255),
            Text_Column TEXT,
            Integer_Column NUMERIC(10),
            Float_Column NUMERIC(10,2),
            Date_Column DATE,
            sysdatecreated timestamp NULL DEFAULT now(),
            sysdatemodified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
        """
    )
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
        create_table(conn)

    finally:
        if conn is not None:
            conn.close()
