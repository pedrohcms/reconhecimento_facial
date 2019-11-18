import psycopg2

DB_NAME = "db_reconhecimento_facial"
DB_USER = "postgres"
DB_PASS = "cdc123"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

p_user_name = ""
p_access_lvl = ""
p_label = ""

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

cur = conn.cursor()

def insert_record (p_user_name,p_access_lvl, p_label):
    cur.execute("INSERT INTO userdata (user_name, access_lvl, label_id) VALUES(%s,%s,%s);",(p_user_name, p_access_lvl, p_label))
    conn.commit()

def select_record (p_label):
    cur.execute("Select * from userdata where label_id like %s;",(p_label,))

    records = cur.fetchall()

    for data in records:
        print("ID: "+ str(data[0]))
        print("Nome usuário: "+ str(data[1]))
        print("Nível de acesso: "+ str(data[2]))
        print("Tag: "+ str(data[3]))
    cur.close()

def close_conn ():
    cur.close()
    conn.close()
select_record("label_test2")

#In this file, the selects and inserts are done with parameters from the "user" of the function.