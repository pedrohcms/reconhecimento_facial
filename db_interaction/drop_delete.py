from psycopg2 import DatabaseError
from db_interaction.connector import conn

cur = conn.cursor()

def drop_table():
    try:
        cur.execute("DROP TABLE IF EXISTS userdata CASCADE;")
        print("Executed!")
        conn.commit()
    except (Exception, DatabaseError) as error:
        print(error)

#"CASCADE" will drop the dependent objects of the table
#For the next commit i will check the need for a close cursor function call here