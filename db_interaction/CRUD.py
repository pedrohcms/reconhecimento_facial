from db_interaction.connector import conn

cur = conn.cursor()

def insert_record (p_user_name, p_access_lvl, p_label):
    cur.execute("INSERT INTO userdata (user_name, access_lvl, label) VALUES(%s,%s,%s);",(p_user_name, p_access_lvl, p_label))
    conn.commit()

    close_conn()

def select_record (p_label):
    cur.execute("Select * from userdata where label like %s;",(p_label,))

    records = cur.fetchall()
    
    close_conn()

    return records[0]

def close_conn ():
    cur.close()
    conn.close()

#select_record('PEDRO_HENRIQUE_CORREA_MOTA_DA_SILVA')

#In this file, the selects and inserts are done with parameters from the "user" of the function.