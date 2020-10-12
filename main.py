import psycopg2

# connect to the db
db_conn = psycopg2.connect(
    host='127.0.0.1',
    database='easytrack_db',
    user='postgres',
    password='nslab123'
)

# cursor
cur = db_conn.cursor()
cur.execute("select id from data.\"2-3\" where data_source_id='10' limit 1")

rows = cur.fetchall()

for r in rows:
    print(r)
    print("\n")

# close the cursor
cur.close()

# close the connection
db_conn.close()
