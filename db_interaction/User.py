from db_interaction.Connector import Connector

class User(Connector):

    def __init__(self):
        super().__init__()
        self.cursor = self.conn.cursor()

    def insert(self, p_user_name, p_access_lvl, p_label):
        self.cursor.execute("INSERT INTO userdata (user_name, access_lvl, label) VALUES(%s,%s,%s);",(p_user_name, p_access_lvl, p_label))
        
    def select(self, p_label):
        self.cursor.execute("Select * from userdata where label like %s;",(p_label,))

        records = cursor.fetchall()

        return records[0]

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()