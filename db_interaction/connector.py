import psycopg2

DB_NAME = "fwkzpiva"
DB_USER = "fwkzpiva"
DB_PASS = "bt89yZ5tQ1Lf26ra_g-F-bYmPZT9_DoJ"
DB_HOST = "motty.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected!")

except expression as identifier:
    print("COnnection failed.")