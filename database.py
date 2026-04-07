import psycopg2

# connect to PostgreSQL
conn = psycopg2.connect(
    dbname="Subscription management system",
    user="postgres",
    password="prajwal",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# query
cur.execute("SELECT * FROM users;")

rows = cur.fetchall()

# print data
for row in rows:
    print(row)

cur.close()
conn.close()