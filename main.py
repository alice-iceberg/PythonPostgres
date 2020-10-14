from psycopg2 import extras as psycopg2_extras
import psycopg2
import time
import os
import base64

_dir = f'images/{int(time.time() * 1000)}'

db_conn = psycopg2.connect(
    host='127.0.0.1',
    database='easytrack_db',
    user='postgres',
    password='nslab123'
)

cur = db_conn.cursor(cursor_factory=psycopg2_extras.DictCursor)
cur.execute('select "value" from "data"."2-3" where data_source_id=25 and "timestamp"=1602664147088;')
rows = cur.fetchall()



if not os.path.exists(_dir):
    os.mkdir(_dir)

if rows is not None:
    counter = 1
    for row in rows:
        image = bytes(row['value'])
        image = base64.b64decode(image)
        with open(f'{_dir}/{counter}.png', 'wb+') as w:
            w.write(image)
        counter += 1

cur.close()
db_conn.close()
