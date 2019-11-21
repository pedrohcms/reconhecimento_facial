from connector import conn
from psycopg2 import DatabaseError

cur = conn.cursor()

def drop_table():
    try:
        cur.execute("DROP TABLE IF EXISTS table_name CASCADE;")
        print("Executed!")
        conn.commit
    except (expression,DatabaseError) as error:
        print(error)


#"CASCADE" will drop the dependent objects of the table
#For the next commit i will check the need for a close cursor function call here