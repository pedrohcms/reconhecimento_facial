from psycopg2 import DatabaseError
from db_interaction.connector import Connector

class UsersMigration(Connector):

    def __init__(self):
        super().__init__()
        self.cursor = self.conn.cursor()

    def up(self):  # Run the migration against the database
        try:
            self.cursor.execute("""CREATE TABLE userdata (
                    id SERIAL PRIMARY KEY, 
                    user_name TEXT, 
                    access_lvl INTEGER,
                    label TEXT
                )
            """)
        except(Exception, DatabaseError) as error:
            print(error)

    def down(self):  # Undo the migration
        try:
            self.cursor.execute("DROP TABLE IF EXISTS userdata CASCADE;")
            print("Executed!")
        except (Exception, DatabaseError) as error:
            print(error)

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
