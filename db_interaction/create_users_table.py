from psycopg2 import DatabaseError
from connector import conn

cur = conn.cursor()

try:
    cur.execute("""CREATE TABLE userdata (
                    id SERIAL PRIMARY KEY, 
                    user_name TEXT, 
                    access_lvl INTEGER,
                    label TEXT
                )
            """)
    cur.close()
    conn.commit()
    conn.close()

except(Exception, DatabaseError) as error:
    print(error)