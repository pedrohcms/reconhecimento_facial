import psycopg2

DB_NAME = "db_reconhecimento_facial"
DB_USER = "postgres"
DB_PASS = "cdc123"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

print("Connected!")

cur = conn.cursor()

cur.execute("""

CREATE TABLE userdata(
    id int primary key not null,
    user_name text not null
)

""")

conn.commit()

print("Created!")

#In this file, the first db interaction is done. Sample sql in execute function.