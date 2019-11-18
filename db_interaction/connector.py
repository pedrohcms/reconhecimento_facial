import psycopg2

DB_NAME = "chmahdbn"
DB_USER = "chmahdbn"
DB_PASS = "5Mi_DUa8WTwqrYPxExWLhb59Iegz8QU2"
DB_HOST = "motty.db.elephantsql.com"
DB_PORT = "5432"

#DB_NAME = "db_reconhecimento_facial"
#DB_USER = "postgres"
#DB_PASS = "cdc123"
#DB_HOST = "127.0.0.1"
#DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected!")

except expression as identifier:
    print("Connection failed.")

#parameters for cloud db connection