from psycopg2 import connect, DatabaseError

#DB_NAME = "db_reconhecimento_facial"
#DB_USER = "postgres"
#DB_PASS = "cdc123"
#DB_HOST = "127.0.0.1"
#DB_PORT = "5432"

class Connector():

    #parameters for cloud db connection
    DB_NAME = "chmahdbn"
    DB_USER = "chmahdbn"
    DB_PASS = "5Mi_DUa8WTwqrYPxExWLhb59Iegz8QU2"
    DB_HOST = "motty.db.elephantsql.com"
    DB_PORT = "5432"

    def __init__(self):
        # The __init__ method connects with the database
        try:
            self.conn = connect(database = Connector.DB_NAME, user = Connector.DB_USER, password = Connector.DB_PASS, host = Connector.DB_HOST, port = Connector.DB_PORT)
            print("Database connected!")

        except (Exception, DatabaseError) as error:
            print("Connection failed.")
            print(error)