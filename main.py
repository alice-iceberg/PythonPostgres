from psycopg2 import extras as psycopg2_extras
import psycopg2
import time
import os
import base64
import pandas as pd

_dir = f'images/{int(time.time() * 1000)}'
PHOTO_TYPE = b'PHOTO'


db_conn = psycopg2.connect(
    host='127.0.0.1',
    database='easytrack_db',
    user='postgres',
    password='nslab123'
)

cur = db_conn.cursor(cursor_factory=psycopg2_extras.DictCursor)


def create_pandas_table(sql_query, database=db_conn):
    table = pd.read_sql_query(sql_query, database)
    return table


cur.execute('select "value" from "data"."2-3" where data_source_id=25 and "timestamp"=1602664808218;')
rows = cur.fetchall()

if not os.path.exists(_dir):
    os.mkdir(_dir)

if rows is not None:
    counter = 1
    for row in rows:
        value_type = bytes(row['value'][-5:])  # check if the type is photo
        if value_type == PHOTO_TYPE:
            print("This is photo")
            image = bytes(row['value'][13:-4])  # between the timestamp and type
            image = base64.b64decode(image)
            with open(f'{_dir}/{counter}.png', 'wb+') as w:
               w.write(image)
            counter += 1

cur.close()
db_conn.close()
